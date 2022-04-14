题目: 给了一个只有开和关的Parentheses, 求最小删除数量括号, 可以使得整个string valid

思路就是用一个stack存index, 遇到'(' 就把index 放进去, 遇到')' 如果stack 有,就pop 掉, 没有就意味着这个')' 需要删除

第一遍结束后, 可以删除掉所有不必要的 ')', 但是还有可能有 '(' 没有match , 这时候, 其实把整个string 反转过, 重复上面过程, 就可以将多余的'(' 也删掉





Time : O(n)
space : O(n)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists = list(s) #spend O(n)
        cnt = 0
        need_close = 0
        for i in range(len(lists)):
            if lists[i] == '(':
                cnt += 1
            elif lists[i] == ')':
                if cnt:
                    cnt -= 1
                else:
                    lists[i] = ''
        
        if cnt:
            for i in range(len(lists) - 1, -1, -1):
                if lists[i] == '(' and cnt:
                    lists[i] = ''
                    cnt -= 1
                if not cnt:
                    break
        
        return ''.join(lists)


Time : O(n)
space : O(n)
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        to_remove = set()
        
        for i, item in enumerate(s):
            if item == '(':
                stack.append(i)
            elif item == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        for i in stack:
            to_remove.add(i)
        
        ans = ''
        for i in range(len(s)):
            if i not in to_remove:
                ans += s[i]
                
        return ans