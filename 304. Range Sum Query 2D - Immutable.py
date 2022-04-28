题目: 一个2d的matrix, 求任意内部的一个矩形的和


解法: 预处理, 给出prefix matrix, 然后计算就可以了

注意这道题最好的写法是创建prefix 的时候多加一行和一列, 这样不存在需要判断越界的问题!!!!



class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.prefix[i][j] = self.prefix[i - 1][j] + self.prefix[i][j - 1] - self.prefix[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1]
        