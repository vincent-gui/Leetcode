题目: 给一个m*n 的matrix, 里面包括了1 和 0, 每次可以翻转一行,或者一列 (从0-> 1, 从1-> 0)
问能否将给的matrix 反转成全部都是0 的matrix 

解法: 
要想翻转成功必须注意, 翻转的pattern 必须是XOX 或者OXO, 

而且, 先翻转row, 再翻转col 的顺序没什么关系, 

以第一行为标准, row1, 和invert_row1, 剩余所有的行必须至少等于这两个之一, 否则没办法成功, 当row 全都变成一样以后, col自然可以变成全0

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        l1, invert_l1 = grid[0], [1 - val for val in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != l1 and grid[i] != invert_l1:
                return False
        return True