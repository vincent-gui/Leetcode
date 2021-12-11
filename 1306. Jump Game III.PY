DFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        return self.dfs(seen, arr, start)
        
        
    def dfs(self, seen, arr, start):
        if start in seen or start < 0 or start >= len(arr):
            return False
        if arr[start] == 0:
            return True
        seen.add(start)
        return self.dfs(seen, arr, start + arr[start]) or self.dfs(seen, arr, start - arr[start])
        
        
        
        
bfs        

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = set([start])
        
        while queue:
            pos = queue.popleft()
            step = arr[pos]
            if step == 0:
                return True
            for num in (1, -1):
                if 0 <= pos + step * num < len(arr) and pos + step * num not in seen:
                    queue.append(pos + step * num)
                    seen.add(pos + step * num)
        
        return False
            
