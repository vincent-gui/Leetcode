内部顺序是
1. 先计算cumsum, 避免添加后, 减去k, 已经出现在里面
2.计算ans
3. 再添加cumsum 进现在的d



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = {0: 1}
        cumSum = 0
        for num in nums:
            cumSum += num
            ans += prefix.get(cumSum - k, 0)
            prefix[cumSum] = prefix.get(cumSum, 0) + 1
        
        return ans