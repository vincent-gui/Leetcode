354. Russian Doll Envelopes

因为是2唯数组, 先按照x 排序, 但是会出现x 相等的时候y不同, 这样其实是需要y 排序的时候用从大到小的顺序排, 因为其实当x 相同的时候, 相同的x 里面只能贡献一个y
[[2,100],[3,200],[4,300],[5,250],[5,400],[5,500],[6,370],[6,360],[7,380]]

不知道是否是因为单调递增, 变成递减以后并不会影响后续连续子序列的结果???

nums.sort(key = lambda k:(k[0], -k[1]))


class Solution(object):
    def maxEnvelopes(self, nums):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        #05/01/2021
        
        """
        if not nums or len(nums) < 1:
            return 0
        
        nums.sort(key = lambda k:(k[0], -k[1]))
		
		切记直接用height , 而不是整个envelopes
        heights = [h[1] for h in nums] #重点是这一行, 为什么排序后直接用高度呢,  是因为排序后会x 值已经从小到大, y 值在相同x 的情况下从大倒小, 例如[200, 300, 500, 400, 600] 这个时候只需要bisect_left 遍历y就可以了
        
        f = []
        
        for h in heights:
            idx = bisect_left(f, h)
            if idx == len(f):
                f.append(h)
            else:
                f[idx] = h
        
        return len(f)
        
        

class Solution(object):
    def maxEnvelopes(self, nums):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        TLE 超时了
        """
        if not nums or len(nums) < 1:
            return 0
        n = len(nums)
        nums.sort() #Nlg(n)
        f = [1 for _ in range(n)]
        
        for i in range(n):#[i 即代表了nums的idx]
            for j in range(i):
                if nums[j][0] < nums[i][0] and nums[j][1] < nums[i][1]:
                    f[i] = max(f[i], f[j] + 1)
        
        return max(f)
        
