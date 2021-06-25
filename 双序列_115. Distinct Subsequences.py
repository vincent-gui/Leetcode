class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
		06/25
        f[i][j] 表示s的前[0...i-1] 里包含了最多多少个t[0...j-1]
        f[i][j] = f[i-1][j] + (f[i-1][j-1] 当s[i-1]==t[j-1])
        rbab
        rb
        其实算到a的时候, 会把之前的rb 最多也存进a里, 所以算最后一个b的时候, 加进去就行了, 这样的计算在dp算最大最小的时候很常见
        边界条件f[i][0] = 1, t为空时, s里至少有一个空串
        """
        
        n, m = len(s), len(t)
        f = [[0 for _ in range (m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if j == 0:
                    f[i][j] = 1 # 边界条件f[i][0] = 1, t为空时, s里至少有一个空串
                    continue
                f[i][j] = f[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
        
        return f[-1][-1]
                
				
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
                