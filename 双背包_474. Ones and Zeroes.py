class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        这是背包, 二维背包
        06/25
        
        f[i][j][k] 表示前i项选出j个0, k个1,最大的subset是几
        选第i 项进入背包, 那么最大就是f[i][j][k] = f[i][j-当前项0的个数][k-当前项1的个数] + 1
        不选第i项进入背包, 那么最大就是f[i][j][k] = f[i-1][j][k] 
        """
        
        size = len(strs)
        f = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)] #这里要注意最里面是[0] * (n + 1) !!!!连续两次犯错了
        #f[0][0][0] = 1
        for i in range(1, size + 1):
            d = {1: 0, 0: 0}
            for letter in strs[i - 1]:
                d[int(letter)] += 1
            
            for j in range(m + 1): #这里必须要考虑到j 与k 为0 的情况
                for k in range(n + 1):
                    if j >= d[0] and k >= d[1]:
                        f[i][j][k] = f[i-1][j - d[0]][k - d[1]] + 1 #这里得是i-1, 因为是前i-1项, 和最后第i项
                    if i > 0:
                        f[i][j][k] = max(f[i][j][k], f[i-1][j][k])
        
        return f[-1][-1][-1]

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        f[i][j][k]: 表示前i个 01串, 最多能有多少个串 被 j个0 和 k个1 组成
        f[i][j][k] = max(f[i-1][j][k], f[i-1][j-strs[i-1][0的个数]][k-strs[i-1][1的个数]] + 1)
        这里有可能会想到, 这个并没有比较到用过多少的0, 1, 但其实f数组本身向前计算的时候f[i-1][j-cnt0[i-1]][k-cnt1[i-1]] 就已经限定了01个个数不会超过!!!! 以后遇到类似的题, 也需要这么考虑
        """
        size = len(strs)
        cnt0, cnt1 = [0]* size, [0] * size
        
        for i, string in enumerate(strs):
            for letter in string:
                if letter == '0':
                    cnt0[i] += 1
                else:
                    cnt1[i] += 1
        
        #注意这里不能把m, 和 n 写反了, 因为代表了0, 和1 的数量限制
        #这里的初始值不用是-1, 因为如果一个都拼不出来, 答案也应该是0, 不可以是-1
        f = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(size + 1)]

        for i in range(1, size + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    if i == 0:
                        f[i][j][k] = 0
                    
                    f[i][j][k] = f[i-1][j][k] if f[i-1][j][k] != -1 else 0
                    if j >= cnt0[i-1] and k >= cnt1[i-1]:
                        f[i][j][k] = max(f[i][j][k], f[i-1][j-cnt0[i-1]][k-cnt1[i-1]] + 1)
        
        return f[-1][-1][-1]
                    
        