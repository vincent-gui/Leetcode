class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, ans, 0)
        
        return ans
    
    def dfs(self, node, ans, depth):
        if not node:
            return
        
        if depth >= len(ans):
            ans.append(node.val)
        self.dfs(node.right, ans, depth + 1)
        self.dfs(node.left, ans, depth + 1)