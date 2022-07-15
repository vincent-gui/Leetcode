题目: 给一个n*m的矩阵, 里面只有1 和0, 每次选择一个翻转, 那么他的上下左右也都翻转, 问最少几步能全部反成0

解法就是暴力bfs

这里有一个trick 就是从就是从一个string 转换回matrix 的时候, string[i] 这个位置求matrix 的i, 和j
i = i // m(m 是每行的长度)
j = i% m(m 是每行的长度)

和几行无关

对于每个matrix的位置做更新, 然后基于当前这个位置,转化成stirng 的index, 然后这个index再找到当前matrix 里的邻居, 更新邻居和自己 #不要漏掉更新自己

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        step = 0
        queue = deque()
        start = ''
        seen = set()
        
        def neighbors(idx):
            out = []
            x, y = idx // m, idx % m
            for di in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = x + di[0], y + di[1]
                if 0 <= dx < n and 0 <= dy < m:
                    out.append(dx * m + dy)
            return out 
        
        def getNext(matrix):
            test = matrix
            for i in range(n * m):
                tmp = [item for item in matrix]
                for pos in neighbors(i) + [i]: #不要漏掉更新自己
                    if tmp[pos] == '1':
                        tmp[pos] = '0'
                    else:
                        tmp[pos] = '1'
                if ''.join(tmp) not in seen:
                    queue.append(''.join(tmp))
                    seen.add(''.join(tmp))
        
        
        
        for i in range(n):
            for j in range(m):
                start += str(mat[i][j])
        queue.append(start)
        seen.add(start)
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                if curr == '0' * (m * n):
                    return step
                getNext(curr)

            step += 1
        return -1
            