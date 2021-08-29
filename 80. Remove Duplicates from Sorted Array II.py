方法1:  fast 和fast - 1 比较, 相等cnt += 1, 不相等cnt= 1
如果cnt <= 2, 就赋值, 前移
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        slow = 1
        
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast - 1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt <= 2:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow 


方法2:  没脑子理解
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]: # 为什么是slow - 2, slow 会停在连续三个相等的数上
                nums[slow] = nums[fast]
                slow += 1
        
        return slow