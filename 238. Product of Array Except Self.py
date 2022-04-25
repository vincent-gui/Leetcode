题目: 给一个数组, 将每一位变成除了他自己的其余的所有数的积

解法, 创建一个ans, p=1

先将p 放入ans, 然后p*=num, 这样只会把前n-1个数放进ans, 然后倒叙重新来一遍


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for num in nums:
            ans.append(p)
            p *= num
            
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
            
        return ans