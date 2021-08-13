解法1: 二分答案, 和378 是同一种类型的二分答案

思路: 这个数组给他分组, 最多能分多少组(len(nums)), 最少是多少组(1组, 就是sum(nums))
在这个最多组和最少组之间, 每一组的和的大家也会变化, 但是和的最小值和最大值是知道的(max(nums), sum(nums))

如果给定每组和不超过多少, 我们就知道最多能够分多少组[正常思维]
反向思维: 给定了多少组, 就得去看每组最少放几个数组, 就是按照令狐冲说的OOXX 的特性

比如说
[7, 2, 5, 10, 8]
分成一组
最大值是10

分成两组最大和数组是
[7],[2, 5, 10, 8] = 25
[7, 2],[5, 10, 8] = 23
[7, 2, 5],[10, 8] = 18
[7, 2, 5, 10],[8] = 24

这里起始就是不断地改变mid(介于10 和sum(nums) 之间)
去检测基于这个每一组的最大值, 能够分成多少组, 再去和题目给定的组数作比较

如果判断出来的组大于了题目给的组, 也就意味着 mid有点小, 需要扩大mid, 从而让更多的数并进同一组
相反, mid 大了就要缩小

重点: 如果mid 做出的结果等于题目给出的怎么办???
比如上面列子中答案是18, 但是如果mid 是19 怎么办!!! 这里需要让end = mid, 类似于排序数组里找target 的第一个位置
不断向左挤压这个结果, 最后找到最靠左的那个满足条件的mid

那么问题就会来了, 怎么样能够保证mid 就是substr 的和??? 同样的问题出现在378 那个题

起始因为是连续的substr, 所以一定会将符合条件的最小的那个mid 找出来, 又因为是连续的, 也就是说
可以把数组看成
[sum1, sum2] 这个sum1 和sum2 是动态变化的, 但是再怎么变, 也是由数组本身组成的, 所以一定会出现再数组内

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.check_group(nums, mid) <= m:
                end = mid
            else:
                start = mid
        if self.check_group(nums, start) <= m:
            return start
        return end
         
    def check_group(self, nums, mid):
        group = 1
        cum_sum = 0
        
        for num in nums:
            if cum_sum + num <= mid:
                cum_sum += num
            else:
                group += 1
                cum_sum = num
        
        return group


解法2 dp
• 求K个人最短需要多少时间抄完前N本书
• 需要知道K-1个人最少需要多少时间抄完前j本书
• 设f[k][i]为前k个抄写员最少需要多少时间抄完前i本书

重点是: 前k-1 个抄写员需要的最短时间抄完前i本书, 

1, 2, 3, 4, ...,    j, j + 1, ...., i 本
[k-1个抄写员负责前j本][第k个抄写员负责后半部分]


计算过程:
最外层遍历k个抄写员/背包/group
中层遍历 书/数组/价值
内层倒序遍历 从i 到j+ 1(起始就是从i 到0 倒序)

f[k][i] = minj=0,…,i{max{f[k-1][j], A[j] +… +A[i-1]}}

初始条件：
– 0个抄写员只能抄0本书
• f[0][0] = 0, f[0][1] = f[0][2] = … = f[0][N] = +∞
– k个抄写员(k>0)需要0时间抄0本书
• f[k][0] = 0 (k > 0)

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        f = [[sys.maxsize] * (len(nums) + 1) for _ in range(m + 1)]
        f[0][0] = 0
        if m > len(nums):
            m = len(nums)
        for k in range(1, m+1): #K 个抄写员, 起始也是背包, k个背包, 怎么样装, 让得到的物品的最大值最小
            f[k][0] = 0
            for i in range(1, len(nums) + 1):
                tmp = 0
                for j in range(i, -1, -1):
                    f[k][i] = min(f[k][i], max(f[k - 1][j], tmp))
                    
                    if j > 0: 
                        tmp += nums[j - 1]
                        
        return f[-1][-1]