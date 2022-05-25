题目: 给了一个字符串, 只有L R X, L 可以和X 交换向左走, R 可以和X 交换向右走

start = "RXXLRXRXL", end = "XRLXXRRLX"

问start 能不能通过转换变成end

一开始看到这个题目, 就觉得是不是dfs, 或者BFS, 但是实在想不出来, 后来发现其实RL 是不能相互换位置的, 

那么移除所有的X 其实剩余的LR 的相对位置应该是一样的, 但是这还是不够的
比如
"LRXXXX"
"XXXXLR" 
其实就是不能转换的, 那么下一步是什么

因为L 只能向左走, 也就意味着从start 里L 的index 一定是要<= L 在end 里的index(移除X 后相同位置的L)
同样的原理适用于R


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start.count('X') != end.count('X'):
            return False
        size = len(start)
        
        i = j = 0
        
        while i < size and j < size: #注意这里是and , 并不需要i he j 都到last index, 比如"LRXXXX" "LXXXXR", 第二个到对胃了, start 里的还是index 1
            if start[i] == 'X':
                i += 1
                continue
            if end[j] == 'X':
                j += 1
                continue
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j: #L 只能向左移动
                return False
            if start[i] == 'R' and i > j: #r 只能向右移动
                return False
            i += 1
            j += 1
        return True