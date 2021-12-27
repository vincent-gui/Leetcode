滑动窗口题目, 不过比较的时候, 注意平均数可能是个小数, 所以target 也得* 1.0


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        if len(arr) < k:
            return 0
        if len(arr) == k:
            if sum(arr) * 1.0 / k >= threshold * 1.0:
                return 1
            else:
                return 0
        
        seen = {}
        start = 0
        ans = 0
        running_sum = sum(arr[:k - 1])
        
        for i in range(k - 1, len(arr)):
            running_sum += arr[i]
            if i - start + 1 > k:
                running_sum -= arr[start]
                start += 1
            if running_sum * 1.0 / k >= threshold * 1.0:
                ans += 1
        
        return ans
            