总结. 和path sum 类似, 同样的模版, 进入dfs 就给加上

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        
        self.dfs(root, '')
        
        return self.ans
        
    
    def dfs(self, node, string):
        
        if not node:
            return
        string += str(node.val)
        if node and not node.left and not node.right:
            self.ans += int(string)
            return
        self.dfs(node.left, string)
        self.dfs(node.right, string)