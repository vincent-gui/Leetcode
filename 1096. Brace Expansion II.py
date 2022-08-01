
题目 带nest 的字母展开, 同1087

{a,b}, {c,d} -> a,b,c,d
{a,b}, {c,d} -> ac, ad, bc, bd

解析 套用stack 模板库

if == {
	stack.append(curr}
	curr = '' or []
elif == }:
	出栈, 并且process
elif == 字母:
	则curr.append
	
但是需要注意的是否要讲string 预先process

[a, b]c
这个时候, a,b 需要先进栈, 但是遇到的c后边的} 并不知道是否需要进栈
所以要预处理成
{{a},{b}}{c}, 只有这样, 遇到c 之前的{ 就可以将[a,b] 入栈


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        stack_op = []
        curr = []
        new = ''
        def product(l1, l2):
            if not l1 and not l2:
                return []
            if not l1 or not l2:
                return l1 or l2
            out = []
            for i in range(len(l1)):
                for j in range(len(l2)):
                    out.append(l1[i] + l2[j])
            
            return out 
        
        for item in expression:
            if item.isalpha():
                new += '{' + item + '}'
            else:
                new += item
        s = '{' + new + '}'
        
        for i in range(len(s)):
            if s[i] == '{':
                stack.append(curr[:])
                stack_op.append(0)
                curr = []
            elif s[i] == ',':
                stack.append(curr[:])
                stack_op.append(1)
                curr = []
            elif s[i].isalpha():
                curr.append(s[i])
            elif s[i] == '}':
                while stack_op[-1] == 1:
                    curr = list(set(stack.pop() + curr))
                    stack_op.pop()
                if stack_op[-1] == 0:
                    curr = product(stack.pop(), curr)
                    stack_op.pop()
        return sorted(curr)