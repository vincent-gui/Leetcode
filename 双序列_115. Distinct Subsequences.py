class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        f[i][j] 表示B 前j 个字符B[0...j-1] 在A 前i个字符[0...i-1]中出现的多少次
        情况一: b的尾巴和A的尾巴相同, 那么f[i][j] = f[i-1][j-1]
        情况二: B[n-1]不和A[m-1]结成对子, 那么f[i][j] = f[i-1][j], 就是说A[i-2] 已经和b[j-1]匹配了
        f[i][j] 是这两种情况相加
        注意f[i][0] = 1, 因为当b为空, B在A中出现次数是1
        """
        
        n, m = len(s), len(t)
        
        
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range( m + 1):
                if j == 0:
                    f[i][j] = 1
                    continue
                f[i][j] = f[i-1][j]
                if s[i - 1] == t[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
        
        return f[-1][-1]
                