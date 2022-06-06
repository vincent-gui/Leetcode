题目: 给一个matrix, 从左上走到右下角, 返回最小的effort

最小effort 的定义是, 从左上, 到右下角的path 中, 相邻两个数的差值的绝对值的最大值

又是一道在所有最大值中求最小的题目


开始的错误思路:
	用(dis, x,y) 作为放进min heap 的tuple, dis 是用max(dis,abs(heights[dx][dy] - heights[x][y])) 求得, 但是下一步就是考虑到同一个点不能重复走(错误的!!!)
	
解法1: 
	如果不用seen set 去track 是否走过, 岂不是每个点都会被走一遍, 也就是 有m*n 个点, 每个点需要遍历m*n 次
	
Dijikstra 算法中, 其实是需要开一个dist 数组的,这个数组展示了从i 到j 能取到的最小的点

需要用priority queue 作为queue, 在这里也需要这个数组

如果curr的dis 比dist[i][j] 的大, 直接舍弃

之后计算出来新的点 和新的点的dis, 如果这个dis 小于dist[new_i][new_j] 则更新dist[new_i][new_j] (default 是无穷大)

time: O(M*N log M*N), , queue 最长mn, 并且需要lgmn 排序

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n, m = len(heights), len(heights[0])
        if n == 1 and m == 1:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * m for _ in range(n)]
        
        queue = [] # priorityQueue
        carry = 0
        heappush(queue, (carry, 0, 0))
        
        while queue:
            carry, x, y = heappop(queue)
            if carry > dist[x][y]: continue
            if x == n - 1 and y == m - 1:
                return carry
            for d in directions:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < n and 0 <= dy < m:
                    new_d = max(carry,abs(heights[dx][dy] - heights[x][y]))
                    if new_d < dist[dx][dy]:
                        dist[dx][dy] = new_d
                        heappush(queue, (new_d, dx, dy))
            
			
解法2:  BFS/DFS + binary search

因为保证了一定有解, 那么就需要从0 ~ 10 ** 6 去判定是否能通过, (这个不需要用priority queue, 普通的就行, 因为能通过, 总有一条路可以通过)
所以扫描过的就不需要再次扫描了!!!! (第一次写漏掉了)


time: m*n *lg(max_height)
space m*n
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        start, end = (0, 0), (n - 1, m - 1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def bfs(dis):
            queue = deque()
            queue.append(start)
            seen = set()
            seen.add(start)
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == end:
                    return True
                for d in directions:
                    dx, dy = d[0] + x, d[1] + y
                    if 0 <= dx < n and 0 <= dy < m and abs(heights[x][y] - heights[dx][dy]) <= dis and (dx, dy) not in seen:
                        queue.append((dx, dy))
                        seen.add((dx, dy))
            
            return False
        
        left, right = 0, 10 ** 6
        
        while left + 1 < right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid
        if bfs(left):
            return left
        return right
                        
            