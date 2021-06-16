class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        f[i][j] 是s[0...i-1] 与p[0...j-1] 是否匹配
        如果p[j] 不是 *, 那么f[i][j] == f[i-1][j-1] 在 i> 0 并且 p[j-1] == '?' 或者s[i-1] == p[j-1]
        
        如果p[j] 是*, 那么就是p的最后一位* 匹配零次或者多次
            零次: f[i][j] = f[i][j-1]
            多次: f[i][j] = f[i-1][j] 这里就是移除s 的最后一位, 继续和p 做匹配
        """ 
        n, m = len(s), len(p)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                    
                #这里不需要计算当i == 0 的时候的f, 交个流程取计算
                '''如果计算, 就是错误的!!!
                if i == 0:
                    f[i][j] = True
                    continue
                '''
                if j == 0:
                    continue
                if p[j-1] != '*':
                    if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '?'):
                        f[i][j] = f[i-1][j-1]
                else:
                    #O个c
                    if j > 0:
                        f[i][j] = f[i][j-1]
                    #多个c
                    if i > 0:
                        f[i][j] = f[i-1][j] or f[i][j]
                    
        return f[-1][-1] 
                    
                    
                    
                    
                    
                    