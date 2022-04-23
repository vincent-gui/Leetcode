题目: 数组里只有0, 和1. 给一个k, 最多反转k次, 让1 连续最长, 求最长的长度

思路: 看到这种提就脑子疼, 但是其实可以用sliding window
最开始思考方式就是遇到0, k -= 1, 但凡k == 0的时候, update ans, 但是k == 0 的那一位后面可能是一串1, 也就意味着如果直到最后都是1, ans 是不会被update 的, 所以其实每一次loop, 都需要update ans, 无论当前是0, 还是1,

还有一点,其实不能check k == 0, 而是需要去考虑 k < 0 作为标准, 这样就可以把 01111 这种情况包括进去

解法: start track 慢指针, i 是快指针, 遇到当前值为0, k -= 1, 如果k < 0, 那么移动慢指针, 每一次循环都需要update ans



class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            ans = max(ans, i - start + 1)
        
        return ans