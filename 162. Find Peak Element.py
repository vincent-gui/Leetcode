总结: 是一道mid 和 mid + 1, mid - 1 比较的题目


重点 就是 其实并不想要知道有几个, 一定会挤在中间

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid - 1] > nums[mid]:
                end = mid
            elif nums[mid + 1] > nums[mid]:
                start = mid
            else:
                return mid
            
        if nums[start] > nums[end]:
            return start
        return end