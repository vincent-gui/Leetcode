class Solution(object):
    def isMatch(self, A, B):
        """
        :type s: str
        :type p: str
        :rtype: bool
        06/24
        f[i][j] 代表A前[0...i-1] 与B前[0...j-1] 是否匹配
        这个题重点在于需要以B 为参考基准, 
        1. 当B[j-1] 是正常字符或者".", 那么只需要与A[i-1] 匹配就行, 相同为true, 不同为false
        2. 当B[j-1] 是 "*", 那么需要考虑,B[j-2] 需要重复一次或者多次, 也就是说A[i-1] 代表的是0个c 还是多个c中的最后一个
            如果是0个c, 那么就只需要看f[i][j-2](因为等于B最后两位都要被扔掉, 所以只需要保证A与B刨除最后两位能够匹配就行)
            如果是多个c, 那么就需要看看去除A最后一个c, 能否和B匹配, 上一次计算已经考虑过B大于等于0个c的情况, 所以B不动
            f[i][j] = f[i-1][j]
        边界条件 f[0][0] = True
        j = 0, 全都是false
        i= 0 交给程序计算
        """
        
        n, m = len(A), len(B)
        
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                if j == 0:
                    continue
                if B[j - 1] != '*':
                    if i > 0 and (A[i - 1] == B[j - 1] or B[j - 1] == '.'):
                        f[i][j] = f[i - 1][j - 1]
                else:
                    #0 c
                    if j > 1:
                        f[i][j] = f[i][j - 2]
                    
                    #multi c
                    if i > 0 and j > 1 and (A[i - 1] == B[j - 2] or B[j - 2] == '.'):
                        f[i][j] = f[i - 1][j] or f[i][j] # 不能忘掉和前一个做or
        return f[-1][-1]
                   

                
                
                




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
                    
                    
                    
                    
                    
                    