题目: 给了一个排序的数组, 和一个k, 问返回的第k个missing number 是什么
例如 nums = [4,7,9,10], k = 1, 那么return 5

二分

这个解法我用了prefix 的数组去存储, 存储到当前index 有多少个missing,
但是 其实nums[i] - nums[j] + 1 就可以表示, [4, 7] -> [4, 5, 6, 7] => 7 - 4 + 1  = 4个数
idx i - j  就代表了数组里出现了几个数
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prefix = [0] #memo how many num miss so far 
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i] - nums[i - 1] - 1)
        
        if k > prefix[-1]:
            return nums[-1] + k - prefix[-1]
        start, end = 0, len(prefix) - 1
        
        
        while start + 1 < end:
            mid = (start + end) // 2
            if prefix[mid] >= k:
                end = mid
            else:
                start = mid
                
        return nums[start] + k - prefix[start]