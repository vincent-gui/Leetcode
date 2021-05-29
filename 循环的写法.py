类型1:
在一个数组里, 取一个可变加1 区间

例 312. Burst Balloons

0........k........n-1
					i
				i,k,j 
			i...k...j 


for i in range(n-1, -1, -1):
	for j in range(i+2, n):
		for k in range(i+1, j):
			....



class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        f[i][j] = max i<k<j {f[i][k] + f[k][j] + a[i] * a[k] * a[j]}
        05/28/2021
        """
        nums = [1] + nums + [1]
        
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i+2, n):
                for k in range(i+1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + nums[i]*nums[j]*nums[k])
        
        return f[0][-1]
		
		
类型2 : 当一个数组内部, 一个idx 并且还有一个length 的情况 

87. Scramble string

注: 当一个数组内部, 一个idx 并且还有一个length 的情况 

如果这个window 起始点的index 是i, 长度是l, 那么终止为止的index 就是i + l - 1

例如
[4,5,6,7,8,9]
[0,1,2,3,4,5]

起始位置是 2, 长度是2, 那么终止位置index 就是 2 + 2 - 1 = 3, 也就是 数字 6,7

如果枚举长度从0 ~ n

那么起始点从0开始的i 的取值范围就是

[0, n - length] 

==> i + length - 1 < n 
==> i + length <= n 
==> i <= n - length

for length in range(0, len(nums)):
	for i in range(0, n - length + 1):
		......
		


class Solution(object):
    def isScramble(self, S, T):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        05/25/2021
        f[i][j][k][h]表示T[k..h]是否由S[i..j]变换而来
        如果区间长度为length, 那么就有j-i == length == h-k
        所以可以变成f[i][j][length] == f[i][j][k] 来表示S 从i开始, T 从j 开始 长度都为k 的, 能否通过互换来得到
        
        
        f[i][j][k] =  #其中w 是 [0 ~ k-1] 的遍历
                (f[i][j][w] and f[i+w][j+w][k-w])
                or
                (f[i][j+k-w][w] and f[i+w][j][k-w])
        
        """
        if len(S) != len(T):
            return False
        
        n = len(S)
        
        f = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if S[i] == T[j]:
                    f[i][j][1] = True
                
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for w in range(1, k+1):
                        if f[i][j][w] and f[i+w][j+w][k-w]:
                            f[i][j][k] = True
                            break
                        if f[i][j+k-w][w] and f[i+w][j][k-w]:
                            f[i][j][k] = True
                            break
        return f[0][0][n]	
