题目: 给了一堆节点, 和节点与节点之间的关系, 求每个节点的所有祖先节点

比如 1是2的父节点, 2是3的父节点, 3的返回值必须是[1, 2]


解法, topo 排序+set去重

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = {i : 0 for i in range(n)} # topo 的时候需要考虑init 的时候是否需要init 那些indegree 为0的节点
        neighbors = {i : [] for i in range(n)}
        nodes = {i : set() for i in range(n)} #用set 保证消除重复节点的加入
        
        for node in edges:
            indegree[node[1]] += 1
            neighbors[node[0]].append(node[1])
        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)
        print(queue)       
        while queue:
            curr = queue.popleft()
            for ni in neighbors[curr]:
                for vertex in nodes[curr]: #这里保证了把所有的祖先节点都加进去
                    nodes[ni].add(vertex)
                nodes[ni].add(curr)
                indegree[ni] -= 1
                if indegree[ni] == 0:
                    queue.append(ni)
        
        return [sorted(nodes[k]) for k in range(n)]