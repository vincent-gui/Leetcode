class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        05/11/2021
		
		https://www.youtube.com/watch?v=kTCymFbU2ok&t=687s
		
		这个解法是下面解法的优化
		0.........i and i+1......j
		f[j] = f[i] + 1 如果 i+1 ~ j 是回文串, 但是, 这里的 i+1 ~ j 是动态变化的, 每一次都是向两边扩大, 所以其实f[j] 会被反复缩小
		注意这里的f[j] 表示切几刀, 下面解法表示最小分成几段
		
		时间 n 平方
		空间 n

        """
        
        n = len(s)
        f = [sys.maxint for _ in range(n)]
        
        for mid in range(n):
            i = j = mid #以mid 为中轴
            while i >= 0 and j < n and s[i] == s[j]:
                f[j] = min(f[j], f[i - 1] + 1 if i > 0 else 0)  #i 除了一次以, 剩余都不是从0 开始, 也就意味着当i reach 到0, 那么从0 ~ mid 和mid ~ j 整个是一个回文串, 所以就是0 
                i -= 1
                j += 1
            
            i, j = mid, mid + 1 #以mid 和mid + 1 为中轴
            while i >= 0 and j < n and s[i] == s[j]:
                f[j] = min(f[j], f[i - 1] + 1 if i > 0 else 0)
                i -= 1
                j += 1
                
        return f[n - 1]
        

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        05/10/2021
        设f[i]为S前i个字符S[0..i-1]最少可以划分成几个回文串
        返回f[-1] - 1, 因为求划几刀
		f[0] = 0
		思路: 先预处理整个串, 以mid 为中心&& 以mid 与mid + 1 为中心 得出从i ~ j 哪些是回文串
		
		
		0.........j and j+1......i
		f[i] = f[j] + 1 如果 j+1 ~ i 是回文串
		
		时间 n 平方
		空间 n 平方
		
        """
        n = len(s)
        
        f = [sys.maxint for _ in range(n + 1)]
        f[0] = 0
        valid = self.isValid(s)
        
        for i in range(1, n + 1): 
            for j in range(i):
                if valid[j][i-1]:
                    f[i] = min(f[i], f[j] + 1)
                    
        return f[-1] -1
    
    def isValid(self, s):
        n = len(s)
        valid = [[False for _ in range(n)] for _ in range(n)]
        
        for mid in range(n):
            i = j = mid
            while i >= 0 and j < n and s[i] == s[j]:
                valid[i][j] = True
                i -= 1
                j += 1
            
            i, j = mid, mid + 1
            while i >= 0 and j < n and s[i] == s[j]:
                valid[i][j] = True
                i -= 1
                j += 1
        return valid
