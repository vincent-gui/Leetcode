这个题 two points

排序以后, 从左开始遍历, i, j, k

如果当前 nums(i) + nums(j) + nums(k) < target, 那么意味着nums(i) + nums(j) + nums(j+1) ....nums(i) + nums(j) + nums(k) 这中间 k-j 中组合都符合要求

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                num = nums[i] + nums[j] + nums[k]
                if num < target:
                    cnt += k - j
                    j += 1
                else:
                    k -= 1
        
        return cnt