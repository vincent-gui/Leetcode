思路: 和find in rotated array 一样, 唯一的区别就是当和nums[start] 相等的时候
start += 1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
            elif nums[mid] > nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                start += 1 #这里是当nums[start] == nums[mid]
        
        if nums[start] == target or nums[end] == target:
            return True
        return False