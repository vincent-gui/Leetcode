

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