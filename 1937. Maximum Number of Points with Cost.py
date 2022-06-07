

题目: 一个矩阵, 每一行挑一个数字, 最后问能挑多大和, 但是每次挑, 需要减掉j 的差值
比如[i-1, 5] 和[i, 9] 就需要减掉 9-5 = 4


我们很容易写出这样的DP写法：

for (int i=0; i<m; i++)
  for (int j=0; j<n; j++)
    for (int k=0; k<n; k++)
      dp[i][j] = max(dp[i][j], dp[i-1][k] - abs(j-k) + points[i][j]);
这样的时间复杂度是o(MNN)，显然会TLE。怎么改进呢？

我们将绝对值符号拆开就会发现

dp[i][j] = max{ dp[i-1][k] + k - j  + points[i][j]};    for k<=j
dp[i][j] = max{ dp[i-1][k] - k + j  + points[i][j]};    for k>=j
我们将dp[i-1][k]+k看做是一个序列，那么dp[i][j]就需要在这个序列的前j个里面挑一个最大的。于是dp[i][j]其实就是这个序列的rolling max value，再加上一个常数项，计算量可以均摊成o(1)。

同理，我们将将dp[i-1][k]-k看做是一个序列，那么dp[i][j]就需要在这个序列的后面n-j个里面挑一个最大的。于是dp[i][j]也是这个序列的rolling max value再加上一个常数项，计算量可以均摊成o(1)。

注意，dp[i][j]最终是需要在两段区间（k<=j 和 k>=j）各自的最大值中挑选一个更大的。

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        f = [[0] * m for _ in range(n)]
        f[0] = points[0]
        
        for i in range(1, n):
            rollingMax = -float('inf') #这里不能是0, 得是负无穷, 因为有可能 f[i - 1][j] - j 是一个负数
            for j in range(m):
                rollingMax = max(rollingMax, f[i - 1][j] + j)
                f[i][j] = max(f[i][j], rollingMax + points[i][j] - j)
               

            rollingMax = -float('inf')#这里不能是0, 得是负无穷
            for j in range(m - 1, -1, -1):
                rollingMax = max(rollingMax, f[i - 1][j] - j)
                f[i][j] = max(f[i][j], rollingMax + points[i][j] + j)
        
        return max(f[-1])
                
                
                
                
        