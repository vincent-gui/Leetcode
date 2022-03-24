这个题没什么特别好说的, 更像是一个medium的题

两个queue, 两个visit, 分别bfs or dfs, 最后遍历一遍heights, 如果同时出现在两个visit里, 就是答案

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(m):
            pacific_queue.append((0, i))
            p_visited.add((0, i))
            atlantic_queue.append((n-1, i))
            a_visited.add((n-1, i))
            
        for j in range(n):
            pacific_queue.append((j, 0))
            p_visited.add((j, 0))
            atlantic_queue.append((j, m-1))
            a_visited.add((j, m-1))
            
        self.bfs(pacific_queue, heights, p_visited)
        self.bfs(atlantic_queue, heights, a_visited)
        
        ans = []
        for i in range(n):
            for j in range(m):
                if (i, j) in p_visited and (i, j) in a_visited:
                    ans.append([i, j])
        
        return ans
    
    def bfs(self, queue, heights, visited):
        directions = [(0, 1), (0, -1), (1, 0),(-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            for i, j in directions:
                dx, dy = x + i, y + j
                if 0 <= dx < len(heights) and 0 <= dy < len(heights[0]) and (dx, dy) not in visited and heights[x][y] <= heights[dx][dy]:
                    queue.append((dx, dy))
                    visited.add((dx, dy))
            
        
        
        
        