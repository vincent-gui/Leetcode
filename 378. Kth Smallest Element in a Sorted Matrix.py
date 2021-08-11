解法: 二分答案, 用matrix 的左上角和右下角的值作为star 和end, 然后求出mid , 计算小于等于mid 的数是否超过了K 个

当大于等于k 时, 让end = mid , 这一步必须这样, 非常重要, 这样可以找到第一个大于等于k 的mid , 并且这个mid 一定在matrix , 别问原因, 不在停不下来
例: [[1,2],[2, 100]]



class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        start, end = matrix[0][0], matrix[-1][-1]
        
        while start + 1 < end:
            mid = (start + end) / 2

            if self.count_less_or_equal(matrix, mid) < k:
                start = mid
            else:
                end = mid
        
        if self.count_less_or_equal(matrix, start) >= k:
            return start
        return end
        
        
        
    def count_less_or_equal(self, matrix, num):
        #从又上到左下
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        cnt = 0
        
        while i < n and j >= 0:
            if matrix[i][j] <= num:
                cnt += j + 1
                i += 1
            else:
                j -= 1
        
        return cnt



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
        