从左下到右上的过程, 因为题目要求, 从上到下递增,从左到右递增

当前值大于target, i -= 1 (减小当前值)
当前值小于target, j += 1 (增大当前值)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(matrix) - 1
        j = 0

        
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        
        return False