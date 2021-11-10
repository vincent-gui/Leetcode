解法 O(h) 时间复杂度

思路: 因为是BST, 所以从上到下while 循环, 然后每一次用当前node 和target 比较, 差值和当前存储的最小作比较

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        
        while root:
            ans = min(root.val, ans, key = lambda x: abs( target - x))
            root = root.left if root.val > target else root.right
        
        return ans 