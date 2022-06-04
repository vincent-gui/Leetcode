题目: 给了一个输入, 然后判定是否valid 的Tic-Tac-Toe  的状态
1. X 数量 必须大于等于O 的数量, 但是也不能超过1
2. X 数量不能超过5, O 的数量不能超过4
3. 如果X 获胜, 则必须O的数量小于X 切差值是1
4. 如果O 获胜, 则必须X 数量等于O 的数量


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def check_win(player):
            for i in range(len(board)):
                if board[i][0] == board[i][1] == board[i][2] == player:
                    return True                        

            #Check the columns
            for i in range(len(board)):
                if board[0][i] == board[1][i] == board[2][i] == player:
                    return True 
										
            #Check the diagonals
            if board[0][0] == board[1][1] == board[2][2]  == player or \
                   board[0][2] == board[1][1] == board[2][0] == player:
                return True
						
            return False
        
        
        cnt_x, cnt_o = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    cnt_o += 1
                elif board[i][j] == 'X':
                    cnt_x += 1
        
        if cnt_x > 5 or cnt_o > 4:
            return False
        if cnt_x - cnt_o > 1 or cnt_x - cnt_o < 0:
            return False
        
        if check_win('X') and cnt_x - cnt_o != 1:
            return False
        
        if check_win('O') and cnt_x != cnt_o:
            return False
        
        return True