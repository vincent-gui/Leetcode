思路: 从左向右, 往stack 里append, 如果当前数比单调栈里最后一个小, 那么就pop, 直到大为止, 放进stack,

注意要用cnt 去track 已经pop 了几个数字, 而且如果最后返回0 要判定, 并且移除前导0

class Solution(object):
    def removeKdigits(self, nums, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        cnt = 0
        for num in nums:
            while stack and num < stack[-1] and cnt < k:
                stack.pop()
                cnt += 1
            stack.append(num)
        
        while cnt < k:
            stack.pop()
            cnt += 1
        
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'