解法1: bottom up 解法, 先定义一个depth 值, 然后左子树的返回值,, 右子树的返回值, 两次update depth

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = [0]
        self.dfs(root, ans)
        
        return ans[0]
        
        
        
    def dfs(self, node, ans):
        #bottom up 
        if not node:
            return 0
        left = self.dfs(node.left, ans)
        right = self.dfs(node.right, ans)
        depth = 1
        if node.left and node.val + 1 == node.left.val:
            depth = max(depth, left + 1)
        if node.right and node.val + 1 == node.right.val:
            depth = max(depth, right + 1)
        ans[0] = max(ans[0], depth)
        return depth
		
		
		
		
		


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 1
        self.dfs(root, 1)
        
        return self.ans
    
    def dfs(self, node, depth):
       #top down
        if not node:
            return
        self.ans = max(self.ans, depth)
        if node.left:
            if node.val == node.left.val - 1:
                self.dfs(node.left, depth + 1)
            else:
                self.dfs(node.left, 1)
        if node.right:
            if node.val == node.right.val - 1:
                self.dfs(node.right, depth + 1)
            else:
                self.dfs(node.right, 1)
        