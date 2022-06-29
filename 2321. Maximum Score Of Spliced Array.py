题目: 给两个数组, 两个数组可以交换一次subarray, 或者不交换, 变形过后, 两个数组能得到的最大的sum

例如 nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20], 需要交换最后两位, 这样数组 一可以得到220

一开始的想法就是两个数组相比较, 找到差值连续正数, 或者连续负数的部分, 交换, 然后比较最大

思想是对的, 但是这个思想是可以简化的

A - B 会得到以B 数组为基础的一串增量数组, 这个数组里, 最大max subarry + Sum(B) 就是可能获得的最大
反过来也是一样

怎样求subarray 最大呢 dp[i] = max(dp[i-1] + nums[i], nums[i]) 


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def maxSubArray(A, B):
            ans = currMax = 0
            for i in range(len(A)):
                currMax = max(0, currMax + A[i] - B[i])
                ans = max(ans, currMax)
            return sum(B) + ans
        
        return max(maxSubArray(nums1, nums2), maxSubArray(nums2, nums1))