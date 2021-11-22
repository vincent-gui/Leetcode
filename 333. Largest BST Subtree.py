# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#解法, bottom up(post order)
这里利用了一个很巧妙的解法, leftMax, leftMin, rightMax, rightMin,
初始设置俩max 为-float('inf'), 俩min为float('inf')
每次node遍历, 就需要更新一次mi, 和mx
        mi = min(lMin, rMin, node.val)
        mx = max(rMax, lMax, node.val)
		
那么可能会问, 但是怎么样保证当前node 也符合bst, 
那么就需要	lMax < node.val < rMin, 左侧最大小于当前node,并且当前node 小于右侧最小

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, node):
        if not node:
            return True, 0, float('inf'), -float('inf')
        
        isLeft, cntL, lMin, lMax = self.dfs(node.left)
        isRight, cntR, rMin, rMax = self.dfs(node.right)
        
        mi = min(lMin, rMin, node.val)
        mx = max(rMax, lMax, node.val)
        
        if isLeft and isRight and lMax < node.val < rMin:
            return True, cntL + cntR + 1, mi, mx
        return False, max(cntL, cntR, 1), mi, mx
        