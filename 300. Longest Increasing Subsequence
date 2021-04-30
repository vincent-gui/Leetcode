class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        04/28/2021
        这个题全网看了很多, 只有花花把这个题讲清楚了
        https://www.youtube.com/watch?v=l2rCz7skAlk
        
        例[3, 4, 1, 2, 8, 5, 6]
        先看下面这两个数组 [1,2,8], [3,4,5]
        哪一个更好, 其实就是在相同长度下, 选取最后一位最小的, 因为假如再来一个6, 就可以组成[3,4,5,6], 但是不可以[1,2,8,6]
        
        当然[1,2,5] 与[3,4,5] 等价, 没什么区别
        
        这里需要建立一个新的DP 数组f
        这个数组里保存元素的意义先忽略不计()
        
        每个数字, 两种选择
        1. 如果最大, 那么append 到数组最后
        2. 在f 中找到比自己大的最小值, 把那个值替换掉, python 用bisect_left
        
        数组f 的长度就是返回结果,
        f[i] 的定义就是最小的结尾数组,数组长度i + 1
        
        例
        3   [3] //[3]
        4   [3,4] // 第一位是3, 表示有一个最优的, 且最长以3为结尾的数组的长度是1, 第二位4 表示最长的单调subsequence 以4作为结尾, 且这个长度是2
        1   [1,4]
        2   [1,2]
        8   [1,2,8]
        5   [1,2,5]
        6   [1,2,5,6]
        
        因为这个数组f 是单调递增的, 所以可以用二分法lg(N)
        时间O(Nlg(N))
        空间O(n)
        
        

        """
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        04/28/2021
        """
        f = []
        for num in nums:
            idx = bisect_left(f, num) #注意这个题是要求严格单调上升, 如果[1,3,3,4] 也算的话, 就得用bisect_right
            if idx == len(f):
                f.append(num)
            else:
                f[idx] = num
        
        return len(f)
        
        


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        04/27/2021
        f[i] =以a[i]结尾的最长上升子序列的长度
        f[j] = max{ 1, f[i] + 1| i < j and a[i] < a[j]}
        思路: 如果a[i] 这个数比f[i-1] 对应的最后一位数大, 那么f[i] = f[i - 1] + 1
        
        计算顺序就是i 从小到大, j 从小到i
        时间O(n平方)
        空间O(n)
        """
        if not nums:
            return 0
        f = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)): #这里遍历不能倒序啊, 因为后边的结果要依赖前面的计算结果
            for j in range(0, i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
        
        return max(f)# 因为并不知道起始点和终止点, 所以只能返回整个数组最大的值
		
		
**********************
打印路径
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        f = [1 for _ in range(len(nums))]
        pi = [-1 for _ in range(len(nums))]
        mx = p = 0
		# p是用来track 最大的f的最后一位来源于哪个idx
		# mx是用来保存返回值, 也就是最大有几个上升
        
        for i in range(len(nums)): #这里遍历不能倒序啊, 因为后边的结果要依赖前面的计算结果
            for j in range(0, i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
                    if f[i] == f[j] + 1: #找到最大的f[i] 是从哪一个j 贡献来的 
                        pi[i] = j
            mx = max(mx, f[i]) #如果mx 小于f[i], 意味着得到了新的最大值, 这个时候p(保存最大值来源的数组最后一位的idx 需要被更新)
            if mx == f[i]:
                p = i
                
        seq = [None for _ in range(mx)]
        for i in range(mx - 1, -1, -1):
            seq[i] = p
            
            p = pi[p]
        
            
    
        return max(f)
        
