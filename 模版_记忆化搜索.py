类型1: 分左右
最后出来的是: min/max(左 + 右, 自己)


312. Burst Balloons



class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}
        return self.dfs(0, n-1, memo, nums)
        
    
    
    def dfs(self, i, j, memo, nums):
        if (i, j) in memo:
            return memo[(i, j)]
        if i + 1 == j:
            memo[(i, j)] = 0
            return 0
        best = 0
        for k in range(i+1, j):
            left = self.dfs(i, k, memo, nums)
            right = self.dfs(k, j, memo, nums)
            best = max(best, left + right + nums[i]*nums[j]*nums[k])
        
        memo[(i, j)] = best
        return best



类型2:  计算calc 或者dfs 函数, 过程中填满f

516. Longest Palindromic Subsequence

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if n == 1:
            return n
        
        self.f = [[-1 for _ in range(n)] for _ in range(n)]
        self.calc(0, n-1, s)
        
        return self.f[0][-1]
    
    def calc(self, i, j, s):
        if self.f[i][j] != -1:
            return 
        if i == j:
            self.f[i][j] = 1
            return
        if i + 1 == j:
            self.f[i][j] = 2 if s[i] == s[j] else 1
            return
        
        self.calc(i+1, j, s)
        self.calc(i, j-1, s)
        self.calc(i+1, j-1, s)
        
        self.f[i][j] = max(self.f[i+1][j], self.f[i][j-1])
        if s[i] == s[j]:
            self.f[i][j] = max(self.f[i][j], self.f[i+1][j-1] + 2)
        