题目: design 一个三子棋

解法就是对于col, 和row, 用数组存储, 对于对角线和反对角线, 用val 存储, 然后验证是否在这四个项目上达到-3 或者3
time : O(1)
space: O(n)
class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antiDiag = 0
        self.n = n
        
        

    def move(self, row: int, col: int, player: int) -> int:
        offset = player * 2 - 3 #either -1, or 1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col + 1 == self.n:
            self.antiDiag += offset
            
        if self.n * offset in (self.diag, self.antiDiag, self.row[row], self.col[col]):
            return player
        return 0


time : O(n)
space: O(n**2)
每次放进去一个, 都需要查询 四个方向

class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None] *  n for _ in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if self.checkRow(row, player) or self.checkCol(col, player) or self.checkDiagonal(row, col, player) or self.checkAntiDiagonal(row, col, player):
            return player
        return 0
               
    def checkRow(self, row, player):
        for j in range(self.n):
            if self.board[row][j] != player:
                return False
        return True
    
    def checkCol(self,  col, player):
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True
    
    def checkDiagonal(self, row, col, player):
        if row != col:
            return False
        for row in range(self.n):
            if self.board[row][row] != player:
                return False
        return True
    
    def checkAntiDiagonal(self, row, col, player):
        if row + col + 1 != self.n:
            return  False
        for row in range(self.n):
            if self.board[row][self.n - row - 1] != player:
                return False
        return True
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)