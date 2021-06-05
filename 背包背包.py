背包问题中, 数组大小和总称重有关

背包1: n个物品不同重量, 一个背包固定重量, 最多能装多少

在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m

数组 = [3,4,8,5]
backpack size = 10

答案: 9

要知道N 个物品是否能拼出重量W(w = 0,1,2...M)
最后一步: 最后一个物品是否进背包

情况1: 如果前N-1 个物品能拼出W, 那么前N 个物品也能拼出W
情况2: 如果前N-1个物品能拼出W-A(n-1), 再加上最后物品重量 A(n-1), 拼出w
​​  
f[i][w] 是前i 个物品能否拼出w

错误L设 f[i] 表示前i 个物品能拼出的最大重量
返例[3,9,5,2] 前三个最大9, 前四个是10

状态方程:
f[i][w] = f[i-1][w] or f[i-1][w-A(i-1)]


w 必须从0开始啊


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        #f[i][w] 意味着前i个物品能否拼出重量w
        #f[i][w] = f[i-1][w] or f[i-1][w-A(i-1)] 

       
        n = len(A)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True

        for i in range(1, n + 1):
            f[i][0] = True
            for w in range(m + 1):
                f[i][w] = f[i-1][w] or f[i][w]

                if w >= A[i-1]: #为什么这里是j>= 是因为只需要保证j-nums[i-1] >= 0. 那么这个差那一位的结果就是f[i][j] 的部分结果
                    f[i][w] = f[i][w] or f[i-1][w-A[i-1]]
        
        for i in range(m, -1, -1):
            if f[-1][i] is True:
                return i


        


---------------------------------



背包5: N 个物品, 不同重量, 给一个背包固定重量, 问有多少种方式装满背包(每种物品可以用1次)

563 · Backpack V

当然，如果能知道这N个物品有多少种方式拼出0，有多少种方式拼出
1，…,有多少种方式拼出Target，也就得到了答案

需要知道N个物品有多少种方式拼出重量W (W =0, 1, …, Target)
• 最后一步：第N个物品（重量A(N-1)）是否进入背包
情况一：用前N-1个物品拼出W
情况二：用前N-1个物品能拼出W- A(N-1) ，再加上最后的物品A(N-1) ，拼出W
情况一的个数+情况二的个数=用前N个物品拼出W的方式

状态：设f[i][w] = 用前i个物品有多少种方式拼出重量w

f[i][w] = f[i-1][w] + f[i-1][w-A(i-1)]

注意
初始条件：
– f[0][0] = 1; 0个物品可以有一种方式拼出重量0
– f[0][1..M] = 0; 0个物品不能拼出大于0的重量
• 边界情况：
– f[i-1][w-A(i-1)]只能在w≥A(i-1)时使用

解法1
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        #f[i][w] 表示用前i个物品有多少种方式拼出w

        n = len(nums)

        f = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        f[0][0] = 1 #前0中物品有1种方式拼出重量0

        for i in range(1, n + 1):
            for j in range(target + 1): #注意这里需要从0开始, 因为前1各物品拼出重量0 的方案也是1 
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]: 
                    f[i][j] += f[i-1][j - nums[i - 1]]
        
        return f[-1][-1]


由于第一种解法, 其实f[i][j] 只和f[i-1][j] 与f[i-1][w-A(i-1)] 有关
所以其实就用下面的方法, 内部从又往左算就行

解法2

		
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        #f[i][j] 表示前i个物品能够拼出j 的个数
        #f[i][j] = f[i-1][j] + f[i-1][w-A(j-1)]
        '''
        if not nums:
            return 0
        n = len(nums)
        f = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        f[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                f[i][j] += f[i-1][j]
                if j >= nums[i - 1]:
                    f[i][j] += f[i-1][j-nums[i-1]]

        return f[-1][-1]
        '''
        if not nums:
            return 0
        n = len(nums)
        
        f = [0 for _ in range(target + 1)] #这里开的数组是根据target的大小
        f[0] = 1 #f[0] 必须是1

        for i in range(1, n + 1):
            #for j in range(target, -1, -1):
                #f[j] = f[j] + f[j - A[i-1]]
            for j in range(target, nums[i-1]-1, -1):  #从又往左算, 为什么到num-1 截至, 因为f[i-1][w-A(i-1)]只能在w≥A(i-1)时使用, 注意这里需要多减一个1, 保证能够取到nums[i-1]
                f[j] += f[j - nums[i-1]]
        
        return f[-1]

377. 背包 6: (Combination Sum IV) 一个背包, n种物品, 不同重量,每种物品可以用无限次. 一个背包, 固定重量.  问有多少种方式装满背包

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        f[i] 就是有多少种组合拼出重量i
        f[i] = f[i-A0] + f[i-A1] + ... + f[i-A(n-1)]
        """
        n = len(nums)
        f = [0 for _ in range(target + 1)]
        f[0] = 1 #这里为什么等于1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    f[i] += f[i-num]
        
        return f[-1]

125 · 背包 2: N个物品不同重量, 不同价值, 每个物品使用一次, 一个背包固定重量, 问背包最大带走多少价值的东西  

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        #f[i][w] 前i各物品拼出的最大总价值
        #f[i][w] = max(f[i-1][w], f[i-1][w - A(i-1)] + v(i-1) and w >= A(i-1) and f[i-1][w - A(i-1)] != -1)

        n = len(A)
        f = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        pi = [[0 for _ in range(m + 1)] for _ in range(n + 1)] #0表示不选

        f[0][0] = 0
        for i in range(1, n + 1):
            f[i][0] = 0
            for w in range(m + 1):
                f[i][w] = f[i-1][w]
                pi[i][w] = 0
                if w >= A[i-1] and f[i-1][w - A[i-1]] != -1:
                    f[i][w] = max(f[i][w], f[i-1][w-A[i-1]] + V[i-1])
                    if f[i][w] == f[i-1][w-A[i-1]] + V[i-1]:
                        pi[i][w] = 1 #为什么只有这个时候让pi[i][w] 等于1 呢, 因为只有斜线的时候才会用, 斜线表示从以前的一个重量跳过来, 尔如果是f[i][w] 从f[i-1][w]来, 那就说明前i-1 个就能够凑出最大价值, 没有必要选取第i个物品
        
        out = max(f[-1])
        j = f[-1].index(out)
        selected = [False for _ in range(n + 1)]

        for i in range(n, 0, -1):
            if pi[i][j] == 1:
                selected[i-1] = True
                j -= A[i-1]
        print pi
        print selected
            
        return out
		
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not A:
            return 0
            
        dp = [[-1] * (m + 1) for _ in range(len(A) + 1)]
        dp[0][0] = 0
        
        for i in range(1, len(A) + 1):
            
            for w in range(m + 1):
                if w == 0:
                    dp[i][w] = 0]
                dp[i][w] = max(dp[i][w], dp[i - 1][w])
                if w >= A[i - 1] and dp[i - 1][w - A[i - 1]] != -1:
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - A[i - 1]] + V[i - 1])
        
        return max(dp[-1])



440 · 背包问题 III

• 题意:
• 给定N种物品，重量分别为正整数A0, A1, …, AN-1，价值分别为正整数V0,
V1, …, VN-1
• 每种物品都有无穷多个
• 一个背包最大承重是正整数M
• 最多能带走多大价值的物品
• 例子：
• 输入：4个物品，重量为2, 3, 5, 7，价值为1, 5, 2, 4. 背包最大承重是10
• 输出：15 （3个物品一，重量3*3=9，价值5*3=15）

f[i][w] = max{f[i-1][w-kA[i-1]] + kV[i-1]}

上面这个式子, 其实就是 
f[i][w] = max(f[i-1][w-0*A[i-1]] + 0 * V[i-1]; f[i-1][w - 1 * A[i-1]] + 1 * V[i-1] + ...+f[i-1][w-k*A[i-1]] + k * V[i-1]) 中的最大值
		= max(f[i-1][x1] + 0*v ; f[i-1][x2] + 1*v; ....; f[i-1][xn] + n*v) 
所以当需要求f[i][w+A2] 的时候, f[i][w+A2] = max(f[i-1][w+A2], f[i][w] + V2)

也就推导出 f[i][w] = max{f[i-1][w], f[i][w-A[i-1]] + v[i-1]}
