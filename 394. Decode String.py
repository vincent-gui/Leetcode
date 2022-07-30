
题目:  分解一个string
Input: s = "3[a2[c]]"
Output: "accaccacc"


就是模板, 

1. 这里一开始想到遇到左括号入栈(这里的入栈是把curr 放进stack 因为可能会遇到 ab2[这样的情况), 
2. 遇到右括号出栈, 出栈的时候, 需要将当前curr 和stack[-1] 做合并, 并且赋值给curr 这一步是灵魂!!!!



class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = []
        curr = ''
        i = 0
        while i < len(s):
            if s[i] in '123456789':
                num = ''
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(curr)
                nums.append(num)
                curr = ''
            elif s[i].isalpha():
                curr += s[i]
            elif s[i] == ']':
                num = int(nums.pop())
                curr = stack[-1] + num * curr
                stack.pop()
            
            i += 1
                
        return curr