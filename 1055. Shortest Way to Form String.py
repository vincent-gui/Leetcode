
题目, 给一个source string , 和一个target string, 问source string 的subsequence, 能否组成target string

问 需要重复source string 几次,
source = 'abc' target = 'abcab'
返回2, 因为target 可以由 两次source 组成



解法:
建造有限状态机(我tm也不知道为啥叫这个名字), 就是对于每个位置, 列出a~z 的下一位的idx, 
然后从source 的0位开始, idx track target 字母的位置, 如果source 里找到target 当前字母, 那么就到下一位去
Time: n + m
https://www.youtube.com/watch?v=UfmEfj3vRtE


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        next = [[-1] * 26 for _ in range(len(source) + 1)]
        n = len(source)
        source = '#' + source
        
        for i in range(n - 1, -1, -1):
            for k in range(26):
                next[i][k] = next[i + 1][k]
            next[i][ord(source[i + 1]) - ord('a')] = i + 1
            #这里next 数组next[i][:] 与next[i+1][:] 应该是完全一样的, 除了next[i][i+1 这一位的字母需要更新] = i+1
        
        j = 0 #stand position at source
        idx = 0 #idx for  target
        ans = 1 #至少走一遍
        
        while idx < len(target):
            if next[j][ord(target[idx]) - ord('a')] != -1:
                j = next[j][ord(target[idx]) - ord('a')]
                idx += 1
            else:
                if j == 0: #stand at 0, but not able find any target[idx]
                    return -1
                j = 0
                ans += 1
        return ans