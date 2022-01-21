题目要求是找到所有钥匙需要最少多少步
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        numOfKeys = 0
        
		#第一步找到初始位置, 找到有几个钥匙
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    x = i
                    y = j
                else:
                    if grid[i][j] in 'abcdef':
                        numOfKeys += 1
                        
        seen = set()
        state = (x, y, '')
        seen.add(state)
        queue = deque([(0, state)])
        
        while queue:
            step, state = queue.popleft()
            x, y, currKeys = state
            if len(currKeys) == numOfKeys:
                return step
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] != '#':
                    new_state = None
                    if grid[dx][dy] in 'ABCDEF' and grid[dx][dy].lower() in currKeys:
                        new_state = (dx, dy, currKeys)
                    elif grid[dx][dy] in '@.':
                        new_state = (dx, dy, currKeys)
                    elif grid[dx][dy] in 'abcdef':
                        new_state = (dx, dy, currKeys + grid[dx][dy] if grid[dx][dy] not in currKeys else currKeys) #重点, 如果key 已经在里面了, 不需要重复添加!!!
                    
                    if new_state and new_state not in seen:
                        seen.add(new_state)
                        queue.append((step + 1, new_state))
        
        return -1