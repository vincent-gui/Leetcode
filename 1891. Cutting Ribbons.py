题目就是给一堆棍子长度, 给一个k 作为参数, 切割棍子, 要求至少有k 个相同长度的棍子, 求相同长度棍子的最大值可以是多少

思路: 二分, k 作为判定参数, 从[0, 10**5] 开始做二分, 找出一个长度后整体扫描一遍, 看看有多少个相同长度的


class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, 10 ** 5
        
        while start + 1 < end:
            mid = (start + end) / 2
            if self.helper(ribbons, mid) < k:
                end = mid
            else:
                start = mid
        if self.helper(ribbons, end) >= k:
            return end
        return start
                
            
            
            
    def helper(self, ribbons, size):
        return sum([r // size for r in ribbons])