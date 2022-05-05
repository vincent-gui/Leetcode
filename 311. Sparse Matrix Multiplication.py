题目: 稀疏矩阵乘法


解法也容易, 稀疏向量乘法用two pointer, 这个就是对稀疏矩阵做一个预处理, 只保留非零项, 

matrix 1 针对每行做一个压缩
matrix 2 针对每列做一个压缩


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def get_row_vectors(matrix):
            vectors = []
            for row in matrix:
                vector = []
                for j, num in enumerate(row):
                    if num != 0:
                        vector.append((j, num))
                vectors.append(vector)
            
            return vectors
        
        def get_col_vectors(matrix):
            vectors = []
            for j in range(len(matrix[0])):
                vector = []
                for i in range(len(matrix)):
                    if matrix[i][j] != 0:
                        vector.append((i, matrix[i][j]))
                vectors.append(vector)
            
            return vectors
        
        def multi(m1, m2):
            i = j = 0
            
            ans = 0
            while i < len(m1) and j < len(m2):
                if m1[i][0] < m2[j][0]:
                    i += 1
                elif m1[i][0] > m2[j][0]:
                    j += 1
                else:
                    ans += m1[i][1] * m2[j][1]
                    i += 1
                    j += 1
            return ans
        
        
        row_vectors = get_row_vectors(mat1)
        col_vectors = get_col_vectors(mat2)
        
        out = []
        for row in row_vectors:
            curr_level = []
            for col in col_vectors:
                curr_level.append(multi(row, col))
            out.append(curr_level)
        return out