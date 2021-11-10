方法1:

inOrder + findKth , 注意findKth模版需要记住

time:O(n) + lg(n) + O(k)
space: O(n)


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nums = self.dfs(root)
        return self.findK(nums, target, k)
        
        
    def dfs(self, node):
        if not node:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)
        
        
        
    def findK(self, nums, target, k):
        ans = []
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        while k > 0:
            left_diff = abs(nums[start] - target) if start >= 0 else float("inf")
            right_diff = abs(nums[end] - target) if end < len(nums) else float("inf")

            if left_diff < right_diff:
                ans.append(nums[start])
                start -= 1
            else:
                ans.append(nums[end])
                end += 1
            k -= 1
        
        return ans