
题目: 三种字母表示三个状态
'A': Absent.
'L': Late.
'P': Present.

问给一个学生n 天的数字, 问多少种状态并且满足下面条件
最多只缺课一天
没有连续三天的迟到

解法: 丧心病狂的6种状态如下

class Solution:
    def checkRecord(self, n: int) -> int:
        #dp00 no A and not end by L
        #dp01 no A and end by 1 L
        #dp02 no A and end by 2 L
        #dp10 1 A and not end by L
        #dp11 1 A and end by 1 L
        #dp12 1 A and end by 2 L
        
        dp00 = [0] * (n + 1)
        dp01 = [0] * (n + 1)
        dp02 = [0] * (n + 1)
        dp10 = [0] * (n + 1)
        dp11 = [0] * (n + 1)
        dp12 = [0] * (n + 1)
        
        dp00[0] = 1
        dp01[0] = 0
        dp02[0] = 0
        dp10[0] = 0
        dp11[0] = 0
        dp12[0] = 0
        M = 1e9+7
        for i in range(1, n + 1):
            dp00[i] = (dp00[i - 1] + dp01[i - 1] + dp02[i - 1]) % M
            dp01[i] = dp00[i - 1]
            dp02[i] = dp01[i - 1]
            dp10[i] = (dp00[i - 1] + dp01[i - 1] + dp02[i - 1] + dp10[i - 1] + dp11[i - 1] + dp12[i - 1]) % M
            dp11[i] = dp10[i - 1]
            dp12[i] = dp11[i - 1]
        
        return int((dp00[-1] + dp01[-1] + dp02[-1] + dp10[-1] + dp11[-1] + dp12[-1] ) % M)