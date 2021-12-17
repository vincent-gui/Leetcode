背包, 如果可以把数组分成两个sub 数组并且和相等, 那么也就意味着 
只需要判定整个数组, 能否拼出target num ,target = sum(nums) / 2

f 数组里存的是true/false, 但是f本身代表了前i 个元素能否拼出重量j


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        
        #f[i][j] 前i 个元素能否拼出重量j
        f = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        f[0][0] = True
        
        for i in range(len(nums) + 1):
            for j in range(target + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                if i == 0 or j == 0:
                    f[i][j] = False
                    continue
                f[i][j] = f[i][j] or f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] = f[i - 1][j - nums[i - 1]] or f[i][j]
        
        return f[-1][-1]