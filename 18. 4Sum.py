思路就是: 排序, 固定1, 2, 循环3, 4

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if len(nums) < 4:
            return []
        ans = []
        
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                start, end = j + 1, len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] + nums[i] + nums[j] == target:
                        ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif nums[start] + nums[end] + nums[i] + nums[j] < target:
                        start += 1
                    else:
                        end -= 1

        return ans
        
		
		
		