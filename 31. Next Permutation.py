思路: 

解题思路是从右往左扫描， 找到第一个降序， 然后把升序部分重新排列(因为是单调递增, >= 所以可以做交换)

1，2，7，5，4，1   排列为 1，2，1，4，5，7
然后从 idx = 2 开始扫描， 第一个比 2 大的数和2 交换
1，4，1，2，5，7

注意！！！ 在从右往左扫描的时候， 第一 i > 0, 第二 idx - 1 >= idx 都是满足条件的
否侧case 【5，1，1】 报错


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        
        while i and nums[i - 1] >= nums[i]: #这里需要的是非递减数列
            i -= 1
        
        self.reverse(nums, i, len(nums) - 1)
        
        for idx in range(i, len(nums)):
            if nums[i-1] < nums[idx]: #这里是i-1, 而不是i
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                break

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            