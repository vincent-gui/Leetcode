思路: 因为所有的偶数只能除以2, 所有的奇数才可以乘以2, 但是会变成一个偶数

便利整个数组, 保持一个最小值, 同时偶数丢进heap, 奇数乘以2 丢进heap

每次pop 一个出来最大的, 用这个和最小的比较, 更新答案, 然后如果这个数可以被2 整除, 那么num /= 2 丢回heap, 如果最大的数都是奇数了, 那么停止, 因为别的数只会越变越小

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        mi_num = inf
        for num in nums:
            if num % 2 == 0:
                heap.append(-num)
            else:
                num *= 2
                heap.append(-num)
            mi_num = min(mi_num, num)
        heapq.heapify(heap)
        min_deviation = inf
        
        while heap:
            curr = heapq.heappop(heap)
            min_deviation = min(min_deviation, -curr - mi_num)
            if curr % 2 == 0:
                mi_num = min(mi_num, -curr // 2)
                heapq.heappush(heap, curr // 2)
            else:
                break
                
        return min_deviation