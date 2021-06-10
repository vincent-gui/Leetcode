class Solution(object):
    def longestCommonSubsequence(self, A, B):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        f[i][j] 表示A 前i个字符A[0...i-1]和B 的前j个字符 B[0...j-1]的最长公共子序列的长度
        f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1] + 1 if A[i-1] == B[j-1])
        """
        
        n, m = len(A), len(B)
        f = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
        
        return f[-1][-1]
        
		
打印路径
class Solution(object):
    def longestCommonSubsequence(self, A, B):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        f[i][j] 表示A 前i个字符A[0...i-1]和B 的前j个字符 B[0...j-1]的最长公共子序列的长度
        f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1] + 1 if A[i-1] == B[j-1])
        """
        
        n, m = len(A), len(B)
        f = [[None for _ in range(m+1)] for _ in range(n+1)]
        pi = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    f[i][j] = 0
                    continue
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if f[i][j] == f[i-1][j]:
                    pi[i][j] = 0
                else:
                    pi[i][j] = 1 
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i][j], f[i-1][j-1] + 1)
                    if f[i][j] == f[i-1][j-1] + 1:
                        pi[i][j] = 2
                    
        ans = ['' for _ in range(f[-1][-1])]
        i, j, p = n, m, f[-1][-1] - 1
        
        while i > 0 and j > 0:
            if pi[i][j] == 0:
                i -= 1
            elif pi[i][j] == 1:
                j -= 1
            elif pi[i][j] == 2: 
                ans[p] = A[i-1] #为什么只有这里添加进res,因为=1或者=0时, 总有一个末尾字符不在, 只有等于2, 才会把末尾两个字符加进去
                p -= 1
                i -= 1
                j -= 1
        
        print ans
        
        return f[-1][-1]
        