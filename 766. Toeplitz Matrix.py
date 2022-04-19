题目: 判定matrix里每一条左上到右下是否相等, 这种矩阵保持同一个diagonal 的方法一般都是 y - x = y1 - x1 

Follow up:
	What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
	What if the matrix is so large that you can only load up a partial row into the memory at once?

	https://leetcode.com/problems/toeplitz-matrix/discuss/271388/Java-Solution-for-Follow-Up-1-and-2
	
	
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
    




class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n - 1, -1, -1):
            if not self.helper(i, 0, matrix):
                return False
        
        for j in range(m):
            if not self.helper(0, j, matrix):
                return False
        
        return True

    def helper(self, i, j, matrix):
        n, m = len(matrix), len(matrix[0])
        check = matrix[i][j]
        while i < n and j < m:
            if matrix[i][j] != check:
                return False
            i += 1
            j += 1
        return True
            