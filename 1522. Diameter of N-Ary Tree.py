题目:
	N 叉数, 返回最长的两个path, 注意这里是边, 而不是node
	
解法,
	和二叉树最长的path 一样,但是这里不是left, right 而是需要遍历所有的children
	



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            first = second = 0
            for child in node.children:
                check = dfs(child)
                if check > first:
                    second = first
                    first = check
                elif check > second:
                    second = check
            
            self.ans = max(self.ans, first + second + 1)
            return first + 1
        self.ans = -1
        dfs(root)
        
        return self.ans - 1 if self.ans != -1 else 0