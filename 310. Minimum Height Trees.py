这个题用的是拓扑排序/扒皮法

统计所有的的node 之间的关系
存成双向关系 , 然后, 遍历所有的neighbor 长度为1 的, 相互删除, 如果neighbor 也变成1了, 进入next_nodes 里, 

当remain node 小于等于2 的时候, 结束, 返回就可以,
因为如果没有环的情况, 答案就只有1个或者2个

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        
        for edge in edges:
            start, end = edge
            neighbors[start].add(end)
            neighbors[end].add(start)
            
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        remain_nodes = n
        
        while remain_nodes > 2:
            remain_nodes -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves