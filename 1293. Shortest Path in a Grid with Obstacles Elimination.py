class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        if k >= n + m - 2:
            return n + m - 2
        
        seen = set()
        start = (0, 0, k)
        queue = deque([(0, start)])
        seen.add(start)
        
        while queue:
            step, status = queue.popleft()
            x, y, eli = status
            if status[0] == n - 1 and status[1] == m - 1:
                return step
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < n and 0 <= dy < m:
                    new_eli = eli - grid[dx][dy]
                    new_status = (dx, dy, new_eli)
                    if new_eli >= 0 and new_status not in seen:
                        seen.add(new_status)
                        queue.append((step + 1, new_status))
        
        return -1
                       