题目: 给了一堆node, 问能否把所有的结点分成两个部分,每个节点所有的联通结点都在另外一部分

1----2
|    |
|    |
3----4
这个时候, (1, 4) (2, 3) 分别成为连个组

解法: 染色法, 遍历所有node(因为不确定是否所有的node都联通), 没有遇到过当前node, color[i] = 1, 然后遍历当前node 的neighbor, 如果neighbor 不在map 里, 赋值 -1, 如果在map里, 则检查是否颜色相反, 如果不是则返回false



class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        queue = deque()
        for i, neighbors in enumerate(graph):
            if i not in color:
                color[i] = 1 
                queue.append(i)
                
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in color:
                            color[neighbor] = -color[curr]
                            queue.append(neighbor)
                        else:
                            if color[neighbor] == color[curr]:
                                return False
        return True