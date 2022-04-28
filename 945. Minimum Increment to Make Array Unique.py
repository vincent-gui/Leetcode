题目, 给一个数组, 说每次可以给任意一位+1, 问最少多少次, 可以让整个数组的数字都变成唯一的


解法, 用一个变量track 当前需要变的数, 再和下一个数字作比较, 差多少补多少, 更新need

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        need = 0
        for num in nums:
            ans += max(need - num, 0)
            need = max(0, need + 1, num + 1)
        
        return ans