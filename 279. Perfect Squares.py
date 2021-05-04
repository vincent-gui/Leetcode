最初思路, f[i] = 0, f[i] = f[i - j] + 1 (如果i - j 是完全平方数)
正确思路是 f[i] = min(f[i - j**2]) + 1

注意!!! 这个题range(1, i**0.5) 的时候, 要写成int(i**0.5) + 1

两种接法,


第一种 BFS, 找到所有在[1, n] 之间的平方数, 然后loop 这个平方数集合, 把剩下的n - 当前平方数 丢进queue里, 当 curr 与平方数里的数相等的时候, 就是最小

注意用两个set 做集合
!!!这里不存在先丢 大数还是小数, 因为其实是分层遍历

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        
        05/01/2021
        BFS
        """
        squares = [i**2 for i in range( int(n**0.5) + 1)]
        ans, q, nq = 1, [n], []

        
        while q:
            for node in q:
                for s in squares:
                    if node == s:
                        return ans
                    if node < s: break
                    nq.append(node - s)
            ans, q, nq = ans + 1, nq, []
        
                     
        
解法二 DP
划分性动态规划, 类似于把n 砍成不同的部分, 但是这里数组开的还是[n+1]

注意!!! j 必须可以等于i, 因为4 可以得出一个完全平方和 4 自己

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        05/01/2021
        DP
        """
        f = [sys.maxint for _ in range(n + 1)]
        f[0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, int(sqrt(i)) + 1): # 注意这里必须是(1, i + 1), 4 可以分为1 个完全平方之和, 所以j 必须能取到2

                f[i] = min(f[i - j**2] + 1, f[i])
                
        return f[-1]
		
		
另一种写法
def numSquares(n):
	dp = [0] + [float('inf')]*n
	for i in range(1, n+1):
		dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
	return dp[n]



FOLLOW UP

有多少种方式把N 表示成完全平方数之和

能不能把N 表示成恰好K 个完全平方数之和

f[i][k] : i 能不能恰好分成k 段, 
f[i][k] = or f[i - j**2][k - 1] 