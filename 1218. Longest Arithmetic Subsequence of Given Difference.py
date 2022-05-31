题目: 给一个数组, 和一个差值, 问最长的连续subsequence 是多长


解法: 用dict 记录, 从左到右, 就可以保证是subsequence

类似于连续和equal K



class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        d = defaultdict(int)
        
        for num in arr:
            if num - difference not in d:
                d[num] = 1
            else:
                d[num] = d[num - difference] + 1
        
        return max(d.values())