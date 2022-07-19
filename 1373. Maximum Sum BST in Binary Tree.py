题目: 找一个tree里最大的bst,并且要求这个bst 的和最大,

主要要注意第三个例子, 也就是说如果最大都是一个负数, 要返回0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = -float('inf')
        def dfs(node):
            if not node:
                return float('inf'), -float('inf'), 0, True
            l_mi, l_mx, l_sum, l_valid = dfs(node.left)
            r_mi, r_mx, r_sum, r_valid = dfs(node.right)
            if l_valid and r_valid and l_mx < node.val < r_mi:
                self.ans = max(self.ans, node.val + l_sum + r_sum)
                return min(l_mi, r_mi, node.val), max(l_mx, r_mx, node.val), node.val + l_sum + r_sum, True
            return min(l_mi, r_mi, node.val), max(l_mx, r_mx, node.val), max(l_sum, r_sum), False
        
        dfs(root)
        return max(0, self.ans)