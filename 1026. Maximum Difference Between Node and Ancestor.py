解法: 对于每一个点, 维护一个子树的最大值和一个最小值

而且这个题bottom up 比较好解

hint, 对于none 的结点 ,应该返回 float('inf'), -float('inf'), 分别代表最小和最大

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #bottom up 
        self.ans = 0
        self.dfs(root)
        
        return self.ans
        
        
    def dfs(self, node):
        if not node:
            return float('inf'), -float('inf')
        
        l_min, l_max = self.dfs(node.left)
        r_min, r_max = self.dfs(node.right)
        
        mi = min(l_min, r_min, node.val)
        mx = max(l_max, r_max, node.val)
        
        self.ans = max(self.ans, abs(node.val - mi), abs(node.val - mx))
        
        return mi, mx