#注意, 这个题的转移方程很可能会设计成从0...i为止的最大值和最小值, !!!错误, 因为这样设置, 没办法backtrack 内部的一些subarray 状态
#需要设置成以i 为最后一个元素的subarry 的最大值和最小值, 这样最后loop 整个f数组就可以找到最大
#类似这样的从一个里面找最大吗要慎重设置f函数


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        06/30
        f[i] means 以i结尾的subarray 的最大值(不是 到i, 最大的product)
        g[i] means 以i结尾的subarray 的最大值(不是 到i, 最小的product)
        """
        
        n = len(nums)
        f = [-sys.maxint for _ in range(n)]
        g = [sys.maxint for _ in range(n)]
        f[0] = g[0] = nums[0]
        
        for i in range(1, n):
            if nums[i] >= 0:
                f[i] = max(nums[i], f[i - 1] * nums[i])
                g[i] = min(nums[i], g[i - 1] * nums[i])
            else:
                f[i] = max(nums[i], g[i - 1] * nums[i])
                g[i] = min(nums[i], f[i - 1] * nums[i])
        
        return max(f)
        
        

        

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        f = [0 for i in range(len(nums))]
        g = [0 for i in range(len(nums))]
        
        f[0] = g[0] = nums[0]
        
        for i in range(1, len(nums)):
            f[i] = max(nums[i], f[i - 1] * nums[i], g[i - 1] * nums[i])
            g[i] = min(nums[i], f[i - 1] * nums[i], g[i - 1] * nums[i])
            
        return max(f)

