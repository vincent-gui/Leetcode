题目 给一个没有排序的整数数组, 返回最小的正整数

Indexing Sort

就是说无论这个数组里有什么, 只需要将当前数组和他的idx 匹配

如[2,3,1,5] , 这个时候需要给数组加一个[0] 变成[0,2,3,1,5]
0 就在idx 0, 那么继续, 
idx 1 上现在是2, 所以就和idx = 2 的数字交换 -> [0,3,2,1,5]
因为现在idx 1 上是3, 那么就和idx = 3 的那个数字交换 -> [0,1,2,3,5]
因为idx 1 == 1, 那么下一个数, 直到5 退出

还有一些比如[0, 1, 2, 2], idx = 3 的时候, 因为idx 2 已经是2, 所以不用继续交换(没意义)
还有需要注意一些num 要小于len(nums) 并且>= 0

最后从头到尾找到那个nums[i] != i, 返回i
如果都没有, 那么就是len(nums)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(len(nums)):
            while nums[i] != i and nums[i] >= 0 and nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                tmp = nums[i]
                nums[i], nums[tmp] = nums[tmp], nums[i]
        
        for i in range(1, len(nums)):
            if nums[i] != i:
                return i
            
        return len(nums)

