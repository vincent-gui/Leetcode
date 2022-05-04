题目: 给了一圈坐标, 返回前k 个离原点最近的点

解法: quick select
和第k 大一样的, 只不过输入变成了k


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k: #必须有着一行, 否则[[1,0],[0,1]] k=2 过不了
            return points
        def get_dis(x, y):
            return x**2 + y**2
        
        def partition(start, end, k):
            left, right = start, end
            p = points[(start + end) // 2]
            pivot = get_dis(p[0], p[1])
            
            while left <= right:
                while left <= right and get_dis(points[left][0], points[left][1]) < pivot:
                    left += 1
                while left <= right and get_dis(points[right][0], points[right][1]) > pivot:
                    right -= 1
                if left <= right:
                    points[left], points[right] = points[right], points[left]
                    left += 1
                    right -= 1
            if k <= right:
                return partition(start, right, k)
            elif k >= left:
                return partition(left, end, k)
            else:
                return k
        idx = partition(0, len(points) - 1, k)
        return points[:k]
                