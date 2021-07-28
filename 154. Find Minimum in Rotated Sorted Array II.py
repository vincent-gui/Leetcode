和题81 类似, 这次是挤压end , 如果mid == end 就end -= 1

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end= 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) / 2
            
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end -= 1
        
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]