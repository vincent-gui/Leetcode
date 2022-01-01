class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        06/05/2021
        思路: 0......k......n, 现在假设k是区间[0+1, n-1]中最后一个被扎破的气球, 那么f[0][n] 就应该等于f[0][k] + f[k][n] + A[0] * A[K] * A[N], 并且这个时候需要给整个A 左右各加一个1, 就能计算整个A
        f[i][j] 表示扎破气球i+1 到j-1 能获得的最大分数
        计算过程: 外层从后向前, 内层从前到后
		
		
		
		01/01/2022
		https://www.youtube.com/watch?v=z3hu2Be92UA
		这个算是bottom up 的计算方法, 
		
		f[i][j] 表示了扎破i+1 到 j-1  这些气球, 
		 f[i][k] + nums[i] * nums[k] * nums[j] + f[k][j]
		其实就表示了
		f[i][k] 前i+1 ~k - 1, 但是不扎破第[i] 和第[k] 个
		
        """
        
        nums = [1] + nums + [1]
        
        n = len(nums)
        f = [[0 for _ in range(n)] for _ in range(n)] # 为什么不用n+1?
        
        for i in range(n-1, -1, -1): #这样写的原因是为了方便j, 与k 的循环
            for j in range(i+2, n): #固定i 以后, 移动j 在区间 i+2 ~ n
                for k in range(i+1, j): #固定j 以后移动k 在区间i ~ j 
                    f[i][j] = max(f[i][j], f[i][k] + nums[i] * nums[k] * nums[j] + f[k][j])
											
                    
        return f[0][n-1]
        
        