和end 作比较, 

if mid >end 大, 那么说明最小值在mid 右侧,
	start = mid
else: # mid 比end 小, 那么说明最小值在mid 左侧
	end = mid 


# 如果有相等怎么办??
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end= 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) / 2
            
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
        
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]