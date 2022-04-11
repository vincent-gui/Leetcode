这个题最开始的思路是每一个点输入以后都判定一次, 判定方法是向上dfs, 向下dfs, 左, 右, 斜线, 反斜线


正确解法是(A 是1, B 是-1)
	查询当前行, 列, 斜线, 反斜线的sum, 如果任意一个abs(sum) == size, 那么就意味着满足了, 可以返回
	分别用两个数组记录
		rows = [row1, row2,..., rowN]
		cols = [col1, col2,..., colN]
		diag = anti_diag = 0
	
	
	最后如果填满格子, 也就意味着input 的长度是size ** 2

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        size = 3
        rows, cols = [0] * size, [0] * size
        diag = anti_diag = 0
        
        player = 1
        
        for row, col in moves:
            rows[row] += player
            cols[col] += player
            
            if row == col:
                diag += player
            if row + col == size - 1:
                anti_diag += player
            
            if any(abs(line) == size for line in (rows[row], cols[col], diag, anti_diag)):
                return 'A' if player == 1 else 'B'
            
            player *= -1
        
        return 'Draw' if len(moves) == size ** 2 else 'Pending'