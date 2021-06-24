class Solution(object):
    def minDistance(self, A, B):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        06/22
        f[i][j] 表示A 前i个字符A[0...i-1] 和B前j个字符[0...j-1] 的最小编辑距离
        四种类型
        1. 给A 添加一个尾巴, 让这个尾巴和B的最后相等 f[i][j-1] + 1, 因为其实就等于A变成B[0...n-2]
        2. 给A 替换一个尾巴, 那么就是f[i-1][j-1] + 1
        3. 把A的尾巴删掉, f[i-1][j] + 1
        4. AB 的尾巴已经相等, 那么就是f[i-1][j-1]
        边界条件:
            f[0][j] = j
            f[i][0] = i
            f[0][0] = 0 空串到空串的编辑距离是0
        
        """
        n, m = len(A), len(B)
        
        f = [[sys.maxint for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = 0 
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                if A[i - 1] == B[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
        return f[-1][-1]

class Solution(object):
    def minDistance(self, A, B):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        f[i][j] 表示A 前i个字符A[0...i-1] 和B前j个字符[0...j-1] 的最小编辑距离
        四种情况
        1. A添上B的尾巴, f[i][j-1] + 1 , 为什么A 添上B 的尾巴反而是f[i][j - 1], 是因为让A[0...i-1] 之后, 再加上一个B的尾巴, 所以其实是让A[0...m-1]变成B[0...n-2], 这个就是f[m][n-1]
        2. A的尾巴换成B的尾巴, f[i-1][j-1] + 1
        3. A的尾巴删除掉, f[i-1][j] + 1
        4. A,B的尾巴相等, f[i-1][j-1] if A[i-1] == B[j-1]
        
        """
        
        n, m = len(A), len(B)
        
        f = [[sys.maxint for _ in range(m+1)] for _ in range(n+1)]
        f[0][0] = 0
        
        
        for i in range(n+1):
            
            for j in range(m+1):
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                
                
                if A[i-1] == B[j-1]:
                    f[i][j] = min(f[i][j], f[i-1][j-1])
                f[i][j] = min(f[i][j], f[i-1][j] + 1, f[i][j-1] + 1, f[i-1][j-1] + 1)
        
        return f[-1][-1]

