背包问题中, 数组大小和总称重有关

背包1

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



背包5

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
            for j in range(target + 1):
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
