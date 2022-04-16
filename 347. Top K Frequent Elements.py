题目:  一个有重复数字的数组, 返回第前k 大的数



方法1: 最小堆
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            
        if k >= len(d):
            return d.keys()
        heap = []    

        for key, v in d.items():
            heapq.heappush(heap, (-v, key))
        ans = []
        while k > 0:
            times, key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
    
        return ans
            
			
			
方法2: quick select
思路就是不用值做交换, 而是用出现的次数作为交换标准, 切记除了和pivot 比较是< >, 剩下都是<= >=

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        uniques = d.keys()
        size = len(uniques)
        idx = self.partition(uniques, 0, size -1, size - k, d) #注意这里传入的是第k 小, 所以要转换成 size-k 传入
        return uniques[size - k:]
        
        
        
    def partition(self, nums, start, end, k, d):
        left, right = start, end
        pivot = d[nums[(start + end) / 2]]
        
        while left <= right:
            while left <= right and d[nums[left]] < pivot:
                left += 1
            while left <= right and d[nums[right]] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right-= 1
        if k <= right:  #这个if 要放在循环外部, 切记切记!!!!
            return self.partition(nums, start, right, k, d)
        elif k >= left:
            return self.partition(nums, left, end, k, d)
        else:
            return k