思路: 思路很直接, 左右两侧返回, 然后一个全局变量track 是否left + right + node.val > self.ans

但是返回需要返回 max(left, right) + node.val , 与0 的更大值

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        self.dfs(root)
        
        return self.ans
        
        
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left + right + node.val > self.ans:
            self.ans = left + right + node.val
        
        return max(max(left, right) + node.val, 0)