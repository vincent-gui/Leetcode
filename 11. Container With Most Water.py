two point, 一个最左, 一个最右, 这个时候最宽, 然后那边矮, 计算一次面积,然后把矮的一边向中间移动一格


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        ans = 0
        
        while start < end:
            if height[start] < height[end]:
                ans = max(ans, height[start] * (end - start))
                start += 1
            else:
                ans = max(ans, height[end] * (end - start))
                end -= 1
        
        return ans