
题目: 给了一个m*n 的格子, 里面的x 表示战舰, 问有几艘战舰
战舰只能是横向或者纵向排列, 并且战舰不相邻

解法, 只关心战舰的第一个格子, 保证上面和左边格子没有, 那么就是一个valid 的答案


time: m*n
space : 1
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i > 0 and board[i - 1][j] == board[i][j]: #验证上面格子没有
                        continue
                    if j > 0 and board[i][j - 1] == board[i][j]: #验证左边格子没有
                        continue
                    ans += 1
        
        return ans