题目: 在一个只有0, 1 的matrix 里, 最长的连续1 是多长

解法: 
一开始想的是对的

每一个当前位置, 分别由 左侧, 上侧, 左上, 和右上决定

这里巧妙地用了default 的默认值避免判断
		
i 这个level 可以用滚动数组优化, 
时间复杂度 O(mn) 空间 O(m), m 是每一个子数组的长度

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        f = defaultdict(int)
        #Horizontal, Vertical,  Diagonal and Anti - diagonal 
        #0, 1, 2, 3
        ans = 0
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    f[(i, j, 0)] = f[(i - 1, j, 0)] + 1
                    f[(i, j, 1)] = f[(i, j - 1, 1)] + 1
                    f[(i, j, 2)] = f[(i - 1, j - 1, 2)] + 1
                    f[(i, j, 3)] = f[(i - 1, j + 1, 3)] + 1
                ans = max([ans] + [f[(i, j, t)] for t in range(4)])
        
        return ans
		
