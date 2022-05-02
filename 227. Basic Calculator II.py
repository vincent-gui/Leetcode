题目: 实现一个基础计算器 + - * /

没有负数

解法: 延迟解法, (除了最后一位)
预先设定sign = '+'

然后如果当前是num 那么num = num * 10 + 当前数字

两个if check, 
	第一个是check 是否是数字, 为了100+20 这种情况
	第二个check 就是考虑(+-*/)这四个符号, 或者!!! 最后一位数字, 因为这里不能再延迟处理
	也就是说, 遇到符号才处理前一个数字, 遇到后一个符号才处理前一个符号, 处理完后update sign 到当前符号
	
注意

l = -3 // 2  #-2
m = int(-3/2) #-1

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(' ', '')
        sign = '+'
        num = 0
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num)) #!!!!重点
                sign = c
                num = 0
                
        return sum(stack)