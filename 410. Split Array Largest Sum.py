解法1: 二分答案
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_group(nums, mid) <= m:
                end = mid
            else:
                start = mid
        if self.check_group(nums, start) <= m:
            return start
        return end
         
    def check_group(self, nums, mid):
        group = 1
        cum_sum = 0
        
        for num in nums:
            if cum_sum + num <= mid:
                cum_sum += num
            else:
                group += 1
                cum_sum = num
        
        return group


解法2 dp

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        f = [[sys.maxsize] * (len(nums) + 1) for _ in range(m + 1)]
        f[0][0] = 0
        if m > len(nums):
            m = len(nums)
        for k in range(1, m+1):
            f[k][0] = 0
            for i in range(1, len(nums) + 1):

                tmp = 0
                for j in range(i, -1, -1):
                    f[k][i] = min(f[k][i], max(f[k - 1][j], tmp))
                    
                    if j > 0: 
                        tmp += nums[j - 1]
                        
        return f[-1][-1]