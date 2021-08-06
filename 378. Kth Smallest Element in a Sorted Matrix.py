
解法: 因为从左到右, 从上到下, 单调递增, 所以从左上开始将数字加入minHeap, 向右和向下探索, 当循环k 次的时候, 就是第k 大的数


class Solution(object):
    def kthSmallest(self, nums, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(nums[0][0], (0, 0))]
        
        n, m = len(nums), len(nums[0])
        check = set((0, 0))
        cnt = 0
        
        while heap:
            num, (x, y) = heapq.heappop(heap)
            cnt += 1
            if cnt == k:
                return num
            if x < n and y + 1 < m and (x, y + 1) not in check:
                heapq.heappush(heap, (nums[x][y + 1], (x, y + 1)))
                check.add((x, y + 1))
            if x + 1 < n and y < m and (x + 1, y) not in check:
                heapq.heappush(heap, (nums[x + 1][y], (x + 1, y)))
                check.add((x + 1, y))
        