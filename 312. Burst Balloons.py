class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        06/05/2021
        思路: 0......k......n, 现在假设k是区间[0+1, n-1]中最后一个被扎破的气球, 那么f[0][n] 就应该等于f[0][k] + f[k][n] + A[0] * A[K] * A[N], 并且这个时候需要给整个A 左右各加一个1, 就能计算整个A
        f[i][j] 表示扎破气球i+1 到j-1 能获得的最大分数
        计算过程: 外层从后向前, 内层从前到后
        """
        
        nums = [1] + nums + [1]
        
        n = len(nums)
        f = [[0 for _ in range(n)] for _ in range(n)] # 为什么不用n+1?
        
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    f[i][j] = max(f[i][k] + f[k][j] + nums[i]*nums[j]*nums[k], f[i][j])
                    
                    
        return f[0][n-1]
        
        