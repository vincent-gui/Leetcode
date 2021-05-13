这个题状态转移方程就是

f[i] = True if f[i - 1] is False or f[i - 2] is False

f[i]表示当前先手, f[i-1] 表示下一个人先手, 当f[i-1] 有一个false, 那么f[i] 必胜

f[0] = false  先手没有子, 必败
f[1] = f[2] = True