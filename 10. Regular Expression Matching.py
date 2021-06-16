'''
注意: 
•空的正则表达式不能匹配长度>0的串
– f[1][0] = … = f[m][0] = FALSE
• 注意：f[0][1..n]也用动态规划计算，但是因为没有A[-1]，所以只能用第
二种情况中的f[i][j-2]

'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        f[i][j] 是s[0...i-1] 与p[0...j-1] 是否匹配
        情况1: p的最后一位是普通字母, 那么f[i][j] = f[i-1][j-1] and s[i-1] == p[j-1]
        情况2: p的最后一位是. 那么f[i][j] = f[i-1][j-1]
        情况3: p的最后一位是* 那么两种情况
            a. 需要消掉p 的最后两位, f[i][j] = f[i][j-2]
            b. p最后一位的* match 多个倒数第二位, 那么这里需要倒数第二位是. 或者f[i-1][j] AND (B[j-2]=‘.’ OR B[j-2]=A[i-1])
        
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
                    if i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                        f[i][j] = f[i-1][j-1]
                else:
                    #O个c
                    if j > 1:
                        f[i][j] = f[i][j-2]
                    #多个c
                    if i > 0 and j > 1 and (p[j-2] == '.' or s[i-1] == p[j-2]):
                        f[i][j] = f[i-1][j] or f[i][j]
                    
        return f[-1][-1]
                    
                    
                    
                    
                    
                    