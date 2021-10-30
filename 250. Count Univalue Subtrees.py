# 思考过程： 每一个leaf node 都是可以计算的， 计算顺序就是左检查， 右检查， 然后没问题ans += 1
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, node):
        if not node:
            return True
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if left and right:
            if node.left and node.val != node.left.val: #这一步就是给只有一个左或者右子树考虑的
                return False
            if node.right and node.val != node.right.val: #这一步就是给只有一个左或者右子树考虑的
                return False
            self.ans += 1
            return True
        else:
            return False