#这个题的代码就是漂亮

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        if not numCourses:
            return ans
        
        indegree = {i: 0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        for child, parent in prerequisites:
            indegree[child] += 1
            graph[parent].append(child)
            
        source = collections.deque([key for key, v in indegree.items() if v == 0])
        
        while source:
            course = source.popleft()
            ans.append(course)
            
            for c in graph[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    source.append(c)
                    
        if len(ans) == numCourses:
            return ans
        return []