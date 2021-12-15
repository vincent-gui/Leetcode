#https://www.youtube.com/watch?v=S-fUTfqrdq8
铺地砖   地砖的解法有三种状态

f[i][j]表示前i个 位置 以j 为状态的拼法有多少种

1. [0]没有突起 - 这一种来源于 f[i-1][0] ,f[i-2][0],f[i - 1][1] + f[i - 1][2],  表示添加一个竖着的砖头 或者两个平行砖头
2. [1]上边突起 - 来源于f[i-2][0], f[i-1][2], 
3. [2]下边突起 - 来源于f[i-2][0], f[i-1][2], 



class Solution:
    def numTilings(self, n: int) -> int:
        
        f = [[0 for _ in range(3)] for _ in range(n + 1)]
        f[0][0] = f[1][0] = 1
        k_mod = 10**9 + 7
        
        for i in range(2, n + 1):
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 1][1] + f[i - 1][2]) % k_mod
            f[i][1] = (f[i - 2][0] + f[i - 1][2]) % k_mod
            f[i][2] = (f[i - 2][0] + f[i - 1][1]) % k_mod
            
        return f[-1][0]