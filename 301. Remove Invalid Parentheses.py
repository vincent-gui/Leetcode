题目: 给一个括号字符串, 问消掉最少的invalid 的字符串, 组成一个valid 的字符串, 问所有组成的可能性


解法: BFS(精妙) 
因为bfs 最先得出的一定是消掉最少并且可以得到valid 的

1. 先把真个字符串放进queue, 然后逐个循环, 如果遇到'(' 或者 ')' 并且没有检查过的, 就放进queue 里

2. 有一个trick 的地方就是found 这个变量, 切实这个变量就保证了遇到第一层valid 就会停止

time: Exponential 
/ˌekspəˈnen(t)SH(ə)l/

space: ex·po·nen·tial
/ˌekspəˈnen(t)SH(ə)l/

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        
        def isValid(s):
            cnt = 0
            for item in s:
                if item == '(':
                    cnt += 1
                elif item == ')':
                    if cnt:
                        cnt -= 1
                    else:
                        return False
            return cnt == 0
    
        if not s:
            return ['']
        queue = deque([s])
        ans, seen = [], set([s])
        found = False
        while queue:
            curr = queue.popleft()
            if isValid(curr):
                ans.append(curr)
                found = True
            elif not found:
                for i in range(len(curr)):
                    if curr[i] in '()':
                        new = curr[:i] + curr[i + 1:]
                        if new not in seen:
                            seen.add(new)
                            queue.append(new)
        return ans