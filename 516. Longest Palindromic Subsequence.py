• 要求S[i..j]的最长回文子序列
• 如果S[i]=S[j]，需要知道S[i+1..j-1]的最长回文子序列
• 否则答案是S[i+1..j]的最长回文子序列或S[i..j-1]的最长回文子序列

f[i][j] = max{f[i+1][j], f[i][j-1], f[i+1][j-1] + 2|S[i]=S[j]}

• 初始条件
– f[0][0] = f[1][1] = … = f[N-1][N-1] = 1
• 一个字母也是一个长度为1的回文串
– 如果S[i] == S[i+1], f[i][i+1] = 2
– 如果S[i] != S[i+1], f[i][i+1] = 1

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        f[i][j] 表示从i 到 j 里最长的回文序列
        f[i][j] = max(f[i+1][j], f[i][j-1]) 掐头去尾,  例 abbbb, abbb与bbbb 里最大的 , 所以是4
        如果s[i] == s[j], 那么 f[i][j] = max(f[i][j], f[i+1][j-1] + 2)
        
        """
        n = len(s)
        if n == 1:
            return 1
         
        f = [[1 for _ in range(n)] for _ in range(n)]
        
        for i in range(n - 1): #为什么要先计算length 为2 的呢, 因为f[1][2] 可能用到f[2][2], f[1][1], f[2][1], 但f[2][1] 是没有意义的, 所以需要先把length 为2 的计算出来
            if s[i] == s[i+1]:
                f[i][i+1] = 2
            else:
                f[i][i+1] = 1
                
                
        for length in range(3, n+1): #这里必须要能够让length 等于长度, 这样才能复盖整个数组
            for i in range(n - length + 1):
                # i is start
                j = i + length - 1 
                # why minus 1, since j is last index, ex: i = 0, 
                #length is 2, j should be 2, that j = i + length - 1
                #j < n ==> i + length - 1 < n ==> i < n - length + 1
                f[i][j] = max(f[i+1][j], f[i][j-1])
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i+1][j-1] + 2)
                    
        return f[0][-1]
                
                

#记忆化, 记忆化就是递归, 和递推的计算顺序相同, 但是会先遇到大的
#递归需要先写出口, 写完所有出口, 写递归表达式,这个题应该f[i][j] 不需要被反复计算, 所以才能用记忆化  


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
        
                   