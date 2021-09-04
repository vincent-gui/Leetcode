思路

	一个N*M循环 扫描竖列, 符合三个取负数保存
	一个N*M循环 扫描横排, 符合三个取负数保存
	
	扫描下落, 用two point, slow 和fast 都从下向上, >0 的交给slow, slow + 1, 最后如果slow > 0, 剩余部分设置成0

解法1
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n, m = len(board), len(board[0])
        crush = True
        
        while crush:
            crush = False #精华步奏, 如果有crush, 再次给True
            
            #check vertical
            for i in range(n - 2):
                for j in range(m):
                    candy = abs(board[i][j]) #这里是处理的精髓, 因为需要考虑到L 型 的crush, 这里可以判断是否有L 型的
                    if candy == 0: continue
                    if candy == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -candy
                        crush = True
            
            #check horizontal
            for i in range(n):
                for j in range(m - 2):
                    candy = abs(board[i][j]) #这里是处理的精髓, 因为需要考虑到L 型 的crush, 这里可以判断是否有L 型的
                    if candy == 0: continue
                    if candy == abs(board[i][j + 1]) == abs(board[i][j + 2]): #即使竖列已经判断过, 但是这里使用了绝对值, 就可以也计算进去
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -candy
                        crush = True
            #gravity where using two point
            
            for j in range(m):
                idx = n - 1 #别写外面了
                for row in range(n - 1, -1, -1):
                    if board[row][j] > 0: #two point 的精髓
                        board[idx][j] = board[row][j]
                        idx -= 1
                while idx >= 0:
                    board[idx][j] = 0
                    idx -= 1
        return board
		
		
解法2 #精华在最后一行
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        crushed = False
		# horizontal crushed
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] == 0: continue
                v = abs(board[i][j])
                if v == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -v
                    crushed = True
        # vertical crushed
        for i in range(m - 2):
            for j in range(n):
                if board[i][j] == 0: continue
                v = abs(board[i][j])
                if v == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -v
                    crushed = True
        # gravity
        if crushed:
            for j in range(n):
                row_index = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[row_index][j] = board[i][j]
                        row_index -= 1
                while row_index >= 0:
                    board[row_index][j] = 0
                    row_index -= 1
        return self.candyCrush(board) if crushed else board #如果crush 过, 继续调用自己, 否则返回board