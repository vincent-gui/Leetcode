讲一讲
	f[i][j][k] 代表第i 行, 机器人1 在位置j, 机器人2 在位置k 的时候, 能获得最大樱桃数目
	不过如果从上往下算, 会需要check 哪些格子能走到, 哪些格子走不到
	所以最好的办法是从下往上算, i 从最底下那一行开始向上计算
	
	每个格子最大的公式就是
	f[i][j][k] = 
		grid[i][j] + grid[i][k] if k != j else 0 #当前格子可以获得的cherry 
		+ max(f[i+1][j][k] for j in [j+1, j, j-1] and k in [k+1, k, k -1]) # + 从底下获得的最大的cherry
	
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        f = [[[0] * m for _ in range(m)] for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m):
                for k in range(m):
                    cherry = grid[i][j]
                    if j != k:
                        cherry += grid[i][k]
                    if i != n - 1:
                        tmp = 0
                        for idx1 in [j, j + 1, j - 1]:
                            for idx2 in [k, k + 1, k - 1]:
                                if 0 <= idx1 < m and 0 <= idx2 < m:
                                    tmp = max(tmp, f[i + 1][idx1][idx2])
                        cherry += tmp
                    f[i][j][k] = cherry
        
        return f[0][0][m - 1]