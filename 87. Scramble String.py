
'''
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
		
		
'''

• 要求T是否由S变换而来
• 需要知道T1是否由S1变换而来的，T2是否由S2变换而来
• 需要知道T1是否由S2变换而来的，T2是否由S1变换而来
• S1, S2, T1, T2长度更短

s  ='abcde'
s1 = 'abc'
s2 = 'de'

t  = 'cabde' 或 t` = 'cdeab'
t1 = 'cab'   或 t1` = 'ab'
t2 = 'de'	 或 t2` = 'cde'

这样就要求 (s1 == t1 and s2 == t2) or (s1 == t2` and s2 == t1`) 





• 子问题
• 状态：f[i][j][k][h]表示T[k..h]是否由S[i..j]变换而来

设f[i][j][k]表示S1能否通过变换成为T1
– S1为S从字符i开始的长度为k的子串
– T1为T从字符j开始的长度为k的子串


• 按照k从小到大的顺序进行计算
– f[i][j][1]，0<=i<N, 0<=j<N
– f[i][j][2]，0<=i<N-1, 0<=j<N-1
–…
– f[0][0][N]
• 答案是f[0][0][N]
• 时间复杂度O(N4)，空间复杂度O(N3)







class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        05/27/2021
        """
        memo = {}
        return self.dfs(s1, s2, memo)
        
    def dfs(self, s, t, memo):
        if (s, t) in memo:
            return memo[(s, t)]
        if len(s) != len(t) or set(s) != set(t):
            memo[(s, t)] = False
            return False

        if s == t:
            memo[(s, t)] = True
            return True
        for i in range(1, len(s)):
            if (self.dfs(s[:i], t[:i], memo) and self.dfs(s[i:], t[i:], memo)) or (self.dfs(s[:i], t[-i:], memo) and self.dfs(s[i:], t[:-i], memo)):
                memo[(s,t)] = True
                return True
        memo[(s, t)] = False
        return False
        


class Solution(object):
    def isScramble(self, S, T):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        05/26/2021
        """
        if len(S) != len(T):
            return False
        
        n = len(S)
        self.f = [[[-1] * (n+1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if S[i] == T[j]:
                    self.f[i][j][1] = True
                else:
                    self.f[i][j][1] = False
        
        self.calc(0, 0, n,S, T)
        
        return self.f[0][0][n]
        
        
        
    def calc(self, i, j, k, S, T):
        if self.f[i][j][k] != -1:
            return self.f[i][j][k]
        
        if set(S[i:i+k]) != set(T[j:j+k]):
            self.f[i][j][k] = False
            return
        
        
        for w in range(1, k):
            self.calc(i, j, w, S, T)
            self.calc(i+w, j+w, k-w, S, T)
            if self.f[i][j][w] is True and self.f[i+w][j+w][k-w] is True:
                
                self.f[i][j][k] = True
                break
                
            self.calc(i, j+k-w, w, S, T)
            self.calc(i+w, j, k-w, S, T)
            if self.f[i][j+k-w][w] is True and self.f[i+w][j][k-w] is True:
                self.f[i][j][k] = True
                break
        if self.f[i][j][k] != True:
            self.f[i][j][k] = False
            
            
                
        
        
        
        

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
        
        
        
        
        
