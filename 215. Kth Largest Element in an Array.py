解法1: 

求top k 用minHeap
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heapq.heappop(heap)
        
解法2: 快排

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)
    
    def partition(self, nums, start, end, k):
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right: #注意这里需要等于, 为了让pivot 的左半部分完全有序
            return self.partition(nums, start, right, k)
        elif k >= left:#注意这里需要等于, 为了让pivot 的右半部分完全有序
            return self.partition(nums, left, end, k)
        else:
            return nums[k] #注意这里其实就是 left = 4, right= 4 然后一交换后变成 5, 3, 需要return 4
                