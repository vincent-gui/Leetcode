解法: 
	先把所有单词建立dict, 然后循环每一个单词, 如果前一个比后一个长, valid = False
	如果遇到前后两个单词同一位置的字母不一样, 那么就是存进graph里
	
	建立indegree(什么时候需要outDegree), 然后从indegree = 0 开始做拓扑排序
	
	最有验证, 所有的长度和graph 的长度是否一样

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''
        self.valid = True
        graph = self.build_graph(words)
        
        if self.valid is False:
            return ''
        
        return self.topoSort(graph)
    
    
    
    def topoSort(self, graph):
        indegree = {key : 0 for key in graph} #什么时候需要记录outdegree呢??
        for key, vals in graph.items():
            for letter in vals:
                indegree[letter] += 1
        
        start = []
        for k, v in indegree.items():
            if v == 0:
                start.append(k)
        
        ans = ''
        queue = Deque(start)
        while queue:
            letter = queue.popleft()
            ans += letter
            for neighbor in graph[letter]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return ans if len(ans) == len(graph) else ''
        
        
    
    def build_graph(self, words):
        #graph with letter and neighbor
        graph = {}
        for word in words:
            for letter in word:
                graph[letter] = []
                
        #base on each word, adding neighbor
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    self.valid = False
                    break
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    break
        return graph
                
        
        