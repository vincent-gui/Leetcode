这个题一开始不容易想, 找不到转移方程

后来看到是动归班最后一堂课的打老怪
f[i][j] 的一位是  !!!以 i, j 为右下角的最大正方形的边长!!! 是边长!!!

基本思路就是f[i][j] 就是以这三个为右下角的最大正方形f[i-1][j], f[i][j-1], f[i-1][j-1], 中找到那个最小的, 如果matrix[i][j] 等于1 , 那么就+ 1
如果matrix[i][j] 等于0, f[i][j] 也就等于0
如果是i== 0 or j == 0 , 那么就是maxtrix[i][j]

最后返回值是遍历整个f, 找到最大的,而不是f[-1][-1] ** 2


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #f[i][j] 是以[i][j] 为 **右下角**的最大正方形, 不是矩形!!
        n, m = len(matrix), len(matrix[0])
        
        f = [[0 for i in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    f[i][j] = int(matrix[i][j])
                    continue
                if matrix[i][j] == '1': 
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
                else:
                    f[i][j] = 0
                    
        ans = 0
        
        for i in range(n):
            for j in range(m):
                ans = max(ans, f[i][j] ** 2)
                
        return ans