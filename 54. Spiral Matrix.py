题目: 一个n*m的矩阵, 求从外向内旋转的数字顺序

解法, 受到题498 的启发, 不需要判断上下左右边界, 用direct 和边界去驱赶direct 的方向, 看code

04/30/2022 注意添加seen, 也可以改变原始matrix 去降低空间复杂


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #(0, 1) -> (1, 0) -> (0, -1) -> (-1, 0)
        n, m = len(matrix), len(matrix[0])
        directs = [(0, 1) ,(1, 0) ,(0, -1) ,(-1, 0)]
        dirt = 0
        seen = set()
        
        if not n or not m:
            return []
        ans = []
        i, j = 0, 0
        for _ in range(n * m):
            ans.append(matrix[i][j])
            seen.add((i, j))
            di, dj = i, j
            x, y = directs[dirt]
            di, dj = di + x, dj + y
            if 0 <= di < n and 0 <= dj < m and (di, dj) not in seen: #如果满足当前要求, 则继续
                i, j = di, dj
            else:
                dirt = (dirt + 1) % 4 #不满足当前要求(意味着越界或者已经查询过了, 那么就需要变换direct的方向
                i += directs[dirt][0]
                j += directs[dirt][1]
        
        return ans