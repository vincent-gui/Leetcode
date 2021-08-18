这个题三个点注意
1. 第一个数字要做重复验证
2. 内部在等于target 以后也要做start& end 的重复验证
3. 外部大结构是<target, start += 1, else end -= 1


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]: #第一个数字要做重复验证
                continue
            target = -nums[i]
            
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                
                    while start < end and nums[start] == nums[start - 1]: #内部在等于target 以后也要做start& end 的重复验证
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:#内部在等于target 以后也要做start& end 的重复验证
                        end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1

        return ans