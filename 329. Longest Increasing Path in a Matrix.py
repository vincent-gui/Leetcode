
题目, 给了一个matrix, 里面都是整数, 问找到最长的升序串

第一个正儿八经自己做出来的hard 题目

解法1: DFS + Memo

因为是找升序串, 所以按照降序查找就可以, 找到最小那个返回1, 然后每次dfs() + 1 , 四个方向选出最大的返回out

可以用lru_cache 做记忆化搜索


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(matrix), len(matrix[0])
        @lru_cache(None)
        def dfs(x, y):
            out = 1
            for di in directions:
                dx, dy = di[0] + x, di[1] + y
                if dx < 0 or dx >= n or dy < 0 or dy >= m: #注意这里并不需要写到最外面, 因为这一行就保证了没有越界发生
                    continue
                if matrix[dx][dy] < matrix[x][y]:
                    out = max(out, dfs(dx, dy) + 1)
            
            return out
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        
        return ans
		
		
解法2 topology sort
思路就是对于每一个当前的数字扫描四个方向, 比他大的就可以给当前的outdegree[x][y] += 1

然后把outdegree == 0 的放进queue, (这里放的是当前最大的node, 针对于他的四个方向, 当然也可以反过来)

然后做分层扫描, 最后返回层数就可以
注意: 只有当curr 的坐标的outdegree 都成0, 才可以加进queue里, 原因是, 可能当前node 还有很远的来路, 
这个来路本身会贡献多个值给ans, 所以如果扫描到就放入queue里, 其实会做重复的扫描, 虽然结果不会改变, 但是会TLE	

from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix) :
        DIR = [0, 1, 0, -1, 0]
        m, n = len(matrix), len(matrix[0])
        
        outDegree = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] <= matrix[r][c]: continue
                    outDegree[r][c] += 1
            
        q = deque([])
        for r in range(m):
            for c in range(n):
                if outDegree[r][c] == 0:
                    q.append([r, c])
                    
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i+1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or matrix[nr][nc] >= matrix[r][c]: continue
                    outDegree[nr][nc] -= 1
                    if outDegree[nr][nc] == 0:
                        q.append([nr, nc])
                    
        return level
matrix = [[9,9,4],[6,6,8],[2,1,1]]        
Solution().longestIncreasingPath(matrix)