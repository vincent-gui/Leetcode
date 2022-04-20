
题目 0 表示空地, 1 表示building, 2 表示block, 只有0可以建房子, 问需要在任意0的位置建立一个房子, 保证到其他房子的距离总和最小

解法, 有点类似于建立邮局那个题, 从现有的building开始建立, 扫描每个空地, 一个dict track 每个位置最小的距离, 另一个dict track 有几个房子可以建立在空地上

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(x, y):
            directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            viewed = [[0] * m for _ in range(n)]
            queue = deque()
            queue.append((x, y, 0))
            viewed[x][y] = 1

            while queue:
                x, y, step = queue.popleft()
                for direct in directs:
                    dx, dy = x + direct[0], y + direct[1]
                    if 0 <= dx < len(grid) and  0 <= dy < len(grid[0]) and grid[dx][dy] == 0 and viewed[dx][dy] != 1:

                        viewed[dx][dy] = 1
                        building[dx][dy] += 1
                        total_dis[dx][dy] += step + 1
                        queue.append((dx, dy, step + 1))

        n, m = len(grid), len(grid[0])
        building = [[0] * m for _ in range(n)] #count how many build reach out to curr land
        total_dis = [[0] * m for _ in range(n)]
        cnt = 0 #check how many building
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    bfs(i, j)
                    cnt += 1
        ans = sys.maxint
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and building[i][j] == cnt:
                    ans = min(ans, total_dis[i][j])
        
        return -1 if ans == sys.maxint else ans
        
        
                
        
        