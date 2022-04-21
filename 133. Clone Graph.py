题目: 克隆一个无向图

解法, 先遍历所有node, 并且保存mapping key node: value copy node
然后再次循环, 添加neighbor


注意点, 每个点只添加自己和邻居, 邻居和自己的关系放在邻居node 里添加

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        mapping = {}
        
        def dfs(curr):
            mapping[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    dfs(neighbor)
                mapping[curr].neighbors.append(mapping[neighbor])
            return mapping[curr]
        
        return dfs(node)



class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return 
        root = node
        mapping = {}
        
        queue = deque()
        queue.append(node)
        
        while queue:
            curr = queue.popleft()
            mapping[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    queue.append(neighbor)
        
        for node, copy_node in mapping.items():
            for neighbor in node.neighbors:
                mapping[node].neighbors.append(mapping[neighbor])
                
        return mapping[root]