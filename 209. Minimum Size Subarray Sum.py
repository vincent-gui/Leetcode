没有太多, 就是滑动窗口

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        O(n)
        """
        start = 0
        amount = 0
        ans = len(nums) + 1
        
        for i, val in enumerate(nums):
            amount += val
            while amount >= target:
                ans = min(i - start + 1, ans)
                amount -= nums[start]
                start += 1
        
        return ans if ans != len(nums) + 1 else 0