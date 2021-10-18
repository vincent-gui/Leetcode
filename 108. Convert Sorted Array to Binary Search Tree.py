class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid = len(nums) / 2
            node = root = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[:mid])
            node.right = self.sortedArrayToBST(nums[mid + 1:])
            return node