题目: 一个n*m的矩阵, 求从外向内旋转的数字顺序

解法, 受到题498 的启发, 不需要判断上下左右边界, 用direct 和边界去驱赶direct 的方向, 看code


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        directs = [(0, 1) ,(1, 0) ,(0, -1) ,(-1, 0)]
        dirt = 0
        
        ans = [[None] * n for _ in range(n)] 
        i, j = 0, 0
        for num in range(1, n * n + 1):
            ans[i][j] = num
            di, dj = i, j  #赋值
            x, y = directs[dirt]
            di, dj = di + x, dj + y  #变动
            if 0 <= di < n and 0 <= dj < n and ans[di][dj] is None:
                i, j = di, dj  #变回来
            else:
                dirt = (dirt + 1) % 4
                i += directs[dirt][0]
                j += directs[dirt][1]
        
        return ans