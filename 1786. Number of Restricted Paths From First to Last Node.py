题目: 给了n 个点(1 ~ n) , 给了一串数组, (u, v, w) 分别意味着, 点u 到点v 的距离是w, (双向的edge)

问: 有多少条路径可以从点1 到点n, 并且保证路径上的点的相对于n点的距离越来越短


以开始没想明白为什么最后可以用dp(lr_cache) 后来发现因为题目要求距离越来越小, 所以意味着整个双向的图变成了单向的图

思路: 建图用 dijkstra , 以n 为起始点, 1为终点建立dist map, 保存每个点相对于n 点的最短距离, 然后dp

注意这里只用到一个 defaultdict 和一个dist 数组
defaultdict 保存是的 {u: (v,w), v:(u, w)} 这样的一对
dist 就是一个长度为(n + 1) 的数组记录每个点最后到n 的距离, 不用dict 是省空间


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        graph = defaultdict(list)
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        print(graph) 
        def dijkstra():
            heap = [(0, n)]
            dist = [float('inf')] * (n + 1) #注意这里直接init 成inf, 就可以省去分别判定已经扫过或者有别的路径比这个短
            dist[n] = 0
            
            while heap:
                d, curr = heapq.heappop(heap)
                for v, w in graph[curr]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(heap, (dist[v], v))
            return dist
        @lru_cache(None)
        def dfs(node):
            if node == n:
                return 1
            out = 0
            for v, w in graph[node]:
                if dist[node] > dist[v]:
                    out = (out + dfs(v)) % modulo
            return out
        dist = dijkstra()
        modulo = 10**9 + 7
        print(dist)
        return dfs(1)