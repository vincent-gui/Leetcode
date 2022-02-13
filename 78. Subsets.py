class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        self.dfs(nums, ans, tmp, 0)
        return ans
        
        
    def dfs(self, nums, ans, tmp, idx):
        ans.append(tmp[:])
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, ans, tmp, i + 1)
            tmp.pop()