题目: 给一个board, 一个单词, 问能否把单词都填进去

要求, 
1.单词只能一个方向, 垂直或者水平
2. 单词必须以边界或者"#"开头
3. 不可以跳格子


解法: https://www.youtube.com/watch?v=WRGUblaxhUo

两层循环, 然后用 k in 4 去track 方向, 一开始想到DFS, 但是dfs 会改变单词方向
模拟就可以
	


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, m = len(board), len(board[0])
        
        
        
        def match(i, j, k, word):
            for t in range(len(word)):
                x, y = i + directions[k][0] * t, j + directions[k][1] * t
                if x < 0 or x >= n or y < 0 or y >= m:
                    return False
                if board[x][y] != ' ' and board[x][y] != word[t]:
                    return False
            x, y = i + directions[k][0] * len(word), j + directions[k][1] * len(word)
            if 0 <= x < n and 0 <= y < m and board[x][y] != '#':
                return False
            return True
        
		
		
		
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0] and board[i][j] != ' ':
                    continue
                for k in range(4):
                    x, y = i - directions[k][0], j - directions[k][1]
                    if 0 <= x < n and 0 <= y < m and board[x][y] != '#':
                        continue
                    if match(i, j, k, word):
                        return True
        return False
    
    