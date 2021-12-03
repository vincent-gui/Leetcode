# f 是什么, 是f[i][j] 代表从i 到j 的最大吗, 
#那么是不是 f[i][j] =  max(f[i-1][j] * nums[i] 与 f[i][j-1] * num[j] )
#O(n**2) 时间复杂度 ???? 什么时候需要这样用???

#有没有更快的, 求连续
#f_mi[i] 是从0开始到i 截至最大的数
#f_mx[i] 是从0开始到i 截至最小的数

#这样会不会出现最大的出现在中间呢, 会, 但是因为每一次都需要和当前nums[i] 作比较, 之前的如果小, mx 数组里就会存入新的nums[i]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_mx = [0] * len(nums)
        f_mi = [0] * len(nums)
        
        f_mx[0] = f_mi[0] = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                f_mx[i] = max(f_mx[i - 1] * nums[i], nums[i])
                f_mi[i] = min(f_mi[i - 1] * nums[i], nums[i])
            else:
                f_mx[i] = max(f_mi[i - 1] * nums[i], nums[i])
                f_mi[i] = min(f_mx[i - 1] * nums[i], nums[i])
        
        return max(f_mx)