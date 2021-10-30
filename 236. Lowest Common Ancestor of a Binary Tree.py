解法: ???

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
        
        
    def dfs(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        if left is None and right is None:
            return None
        if left and right:
            return node 
        if left or right:
            return left or right
        