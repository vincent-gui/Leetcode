思路, 一开始想着是滑动窗口, 后来发现并不可以, 因为不知道什么时候才可以移动slow 指针
	prefixSum, 但其实并不完全是
	
	遇到0 就-= 1, 遇到 1 就+= 1, 这样有一个变量一直track so far 的总和, 用一个dict 去track 之前和的位置, 就可以求出最大
	
	注意点: 这个题也出现要预设 d = {0:0} 的情况, 类似的题是 560. Subarray Sum Equals K
	但是这个题 在存index 的时候需要+ 1, 因为0:0 是初始点, 第一个书其实的位置是1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        d = {0: 0}
        
        curr = 0
        
        for i in range(len(nums)):
            curr +=  nums[i] or -1
            if curr not in d:
                d[curr] = i + 1
            else:
                ans = max(ans, i - d[curr] + 1)
        
        return ans