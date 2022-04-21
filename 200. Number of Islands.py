
题目: 找有几个岛屿

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            for x, y in offsets:
                dfs(i + x, j + y)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        
        return ans