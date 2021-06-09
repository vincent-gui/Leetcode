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
        