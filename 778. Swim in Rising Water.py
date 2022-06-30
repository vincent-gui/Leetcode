题目: 

给了一个矩阵, 每个位置代表了海拔高度, 现在说, 每一秒钟, 因为下雨, 每个格子的高度最少都会变成t, 如果大于t 则保持不变

0, 2    1, 2    2, 2
1, 3 -> 1, 3 -> 2, 3

问最少需要多少时间, 就可以让人从左上角, 游到右下角(一次游泳可以拐弯, 无限距离)

其实题目问的是, 求从左上到右下路径上的最大值, 最小的数

解法1 binary search + bfs/dfs 
注意start 要设置成grid[0][0],因为例子 [[3, 2], [1, 0]], 需要返回3

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        def bfs(mark):
            seen = set()
            queue = deque()
            queue.append((0, 0))
            seen.add((0, 0))
            
            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for di in directions:
                    dx, dy = di[0] + x, di[1] + y
                    if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in seen and mark >= grid[dx][dy]:
                        queue.append((dx, dy))
                        seen.add((dx, dy))

            return False
        
        start, end = grid[0][0], n**2
        
        while start + 1 < end:
            mid = (start + end) // 2
            if bfs(mid):
                end = mid
            else:
                start = mid
        
        if bfs(start):
            return start
        return end


解法2, 这个太骚气, 牛逼, 可以理解为一个dijkstra 的问题, 不是很好想, 把当前遇到的最大值得最小

普通的 是从A 到B 的权重
这个题是要达到当前点需要的总权重是什么

https://www.youtube.com/watch?v=umdk98ynLSY


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq, ans, n = [(grid[0][0], 0, 0)], 0, len(grid)
        seen = set([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while pq:
            curr, x, y = heappop(pq)
            ans = max(ans, curr)
            if x == n - 1 and y == n - 1:
                return ans
            for di in directions:
                dx, dy = x + di[0], y + di[1]
                if 0 <= dx < n and 0 <= dy < n and (dx, dy) not in seen:
                    heappush(pq, (grid[dx][dy], dx, dy))
                    seen.add((dx,dy))