题目: make 一个最大岛屿, 意思就是有一堆岛屿, 现在最多变更一个空地成岛屿, 能获得最大岛屿面积


解法: 遍历每个岛屿, 但是处理的时候有点技巧, 给每个岛屿编号(相同的岛屿全部都变成同一个数字), 并且用一个dict 来保存 {岛屿: 岛屿面积},

最后再遍历所有空地, 对每个空地做一轮上下左右, 如果能到别的岛屿上, 那么把别的岛编号记下来, 最后做一个sum, 每次再求最大


有一个edge case, 

[[1,1]
 [1, 1]
]
这个时候最后一步遍历0 会直接跳过, 所以需要判定一下是不是ans 和初始值相同, 如果相同则返回m*n


https://leetcode.com/problems/making-a-large-island/discuss/1375940/Python-dfs-with-connected-components-explained


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direct in directs:
                dx, dy = i + direct[0], j + direct[1]
                if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == 1:
                    grid[dx][dy] = island
                    mapping[island] += 1
                    dfs(dx, dy)
                    
        if not grid or len(grid[0]) == 0:
            return 0
        
        ans = 0
        mapping = {}
        island = 2 # because 0 and 1 used by grid
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = island
                    mapping[island] = 1
                    dfs(i, j)
                    island += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    neighbors = set()
                    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for direct in directs:
                        dx, dy = i + direct[0], j + direct[1]
                        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] in mapping:
                            neighbors.add(grid[dx][dy])
                    ans = max(ans, sum(mapping[k] for k in neighbors) + 1)
        return ans if ans != 0 else len(grid) * len(grid[0])