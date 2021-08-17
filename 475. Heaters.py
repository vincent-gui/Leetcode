思路: 到这座, 要求找到最小的半径, 可以cover所有house,  如果一个一个尝试半径 属于二分答案, 不是很容易下手

将所有的heaters 排序, 然后便利houses, 需要最大的距离就是答案


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        
        for house in houses:
            ans = max(ans, self.find_heater(house, heaters))    
        
        return ans
    
    
    def find_heater(self, house, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == house:
                return 0
            elif nums[mid] > house:
                end = mid
            else:
                start = mid
                
        return abs(nums[start] - house) if abs(nums[start] - house) < abs(nums[end] - house) else abs(nums[end] - house)