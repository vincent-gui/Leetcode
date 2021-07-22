class Solution():
    def findKthLargest(self, nums, k):
        if not nums or len(nums) == 0:
            return 

        self.partition(nums, 0, len(nums) - 1)
        
        return nums[len(nums) - k]
        
    def partition(self, nums, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = nums[(start + end) / 2]
        while left <= right:

            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.partition(nums, start, right)
        self.partition(nums, left, end)
