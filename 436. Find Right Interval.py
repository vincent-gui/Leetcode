二分, 先排序, 再二分查找

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([[start, end, i] for i, [start, end] in enumerate(intervals)])
        starts = [i for i, j, k in intervals]
        
        ans = [-1] * len(intervals)
        
        for start, end, i in intervals:
            idx = bisect.bisect_left(starts, end)
            if idx < len(starts):
                ans[i] = intervals[idx][2]
        
        return ans