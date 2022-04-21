题目: 给一个matrix, 和一个字符串, 问再这个矩阵中,能否找到这个字符

解法: 就dfs, 如果string 是空, 就返回true, 

步奏就是丢进去, 比较第一个字母, 如果相同, 那么对于剩下的字符穿继续dfs有就有, 没有backtrack, 需要一个seen 去track 是否已经遍历过

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        
        def dfs(i, j, word):
            if not word:
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[0] or seen[i][j] is True:
                return False
            back = False
            seen[i][j] = True
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                back = back or dfs(i + x, j + y, word[1:])
            seen[i][j] = False
            return back
        
        n, m = len(board), len(board[0])
        seen = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False