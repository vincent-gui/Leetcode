题目:
	从一个matrix 的左上角走到右下角的最短距离, 可以朝八个方向走, 只能走0, 不能走1
	
解法:
	需要判断是否grid 为空, 或者grid[0] 是否为空
	还需要判断是否[0][0] == 1, 如果是, 返回-1
	
	剩下标准bfs
	
	
注意:
However, like all in-place algorithms, overwriting the input can cause problems. Here are a couple of possible scenarios you need to consider.

1. That the algorithm is running in a * multithreaded* environment, and it does not have exclusive access to the grid. Other threads might need to read the grid too, and might not expect it to be modified.

2. That there is only a single thread or the algorithm has exclusive access to the grid while running, but the grid might need to be reused later or by another thread once the lock has been released.

For the second scenario, Approach 1 could be modified to restore the grid—simply loop over it at the end, replacing all numbers that are greater than 1 with a 0, and additionally set the top-left cell to a 0.

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return -1
        if grid[0][0] == 1:
            return -1
        
        points = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        ans = 1
        n, m = len(grid), len(grid[0])
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if x == n - 1 and y == m - 1:
                    return ans
                for point in points:
                    dx, dy = point[0] + x, point[1] + y
                    if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 0:
                        grid[dx][dy] = 1
                        queue.append((dx, dy))
            ans += 1

        
        return -1