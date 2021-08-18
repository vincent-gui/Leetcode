思路:
数组排序, 第一个循环, 然后start end
将amount = nums[i] + nums[start] + nums[end] 算出后, 比较target, 只要ans is none 或者小于现有结果, 就代替
下一步: 大于target end -= 1 else start += 1


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = None
        nums.sort()
        
        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                amount = nums[i] + nums[start] + nums[end]
                if ans is None or abs(target - ans) > abs(target - amount):
                    ans = amount
                
                if amount > target:
                    end -= 1
                else:
                    start += 1
        
        return ans