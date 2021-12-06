思路:
	对于每一个node, 意味着需要选取孩子还是自己, 也就意味着, 这个题其实用了return的 (), 作为一个迭代的数组, 属于bottom up 的判断模式
	
	从下到上, 累加计算
	rober 的计算是 node 自己 + 左孩子不抢 + 右孩子不抢
	non rober 的计算是 左孩子最大 + 右孩子最大

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))
        
        
    def dfs(self, node):
        if not node:
            return (0, 0)
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        rober = node.val + left[1] + right[1]
        non_rober = max(left) + max(right)
        
        return (rober, non_rober)