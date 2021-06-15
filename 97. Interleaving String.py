class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        f[s][i][j] 就是s3 的前s个字符是否由s1的前[0...i-1] 和s2的前[0...j-1] 交错形成
        s = i+j
        f[i][j] 就是s3 的前i+j个字符是否由s1的前[0...i-1] 和s2的前[0...j-1] 交错形成
        f[i][j] = (f[i-1][j] and s3[i+j-1] == s1[i-1]) or (f[i][j-1] and s3[i+j-1] == s2[j-1])
        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        n, m = len(s1), len(s2)
        
        f = [[False for _ in range(m+1)] for _ in range(n+1)] #这里的循环和下面的循环顺序要一致, 否则index 报错
        
        f[0][0] = True
        
        for i in range(n+1): #必须从0开始, 因为要计算完全从一个string 得到结果
            for j in range(m+1):#必须从0开始, 因为要计算完全从一个string 得到结果
                if i > 0 and f[i-1][j] and s3[i+j-1] == s1[i-1]:
                    f[i][j] = True
                if j > 0 and f[i][j-1] and s3[i+j-1] == s2[j-1]:
                    f[i][j] = True
                
        
        return f[-1][-1]