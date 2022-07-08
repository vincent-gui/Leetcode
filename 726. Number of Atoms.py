题目: 给了一串字符, 里面包括了元素名字, 包括了几个元素, 可能还有括号

让返回一串被展开的元素, 并且按照字母排序


遇到括号这种, 肯定就是stack 跑不了

先写大框架

if 遇到 (  
	那么把当前curr 加入stack, curr = 新的空集合
	
elif 遇到):
	这个时候因为括号关闭了, 那么处理现在的curr
	并且把现在的curr 和stack 最后一项合并
	
else: 
	就是中间需要被处理的字母了
	一步一步实现就行
	
返回


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        
        stack = []
        curr = {}
        i = 0 
        # push into stack
        while i < len(formula):
            if formula[i] == '(':
                stack.append(curr)
                curr = {}
        # pop from stack 
            elif formula[i] == ')':
                j = i + 1
                #check any num after )
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                cnt = 0
                #)后没有数字
                if j == i + 1:
                    cnt = 1
                else:
                    cnt = int(formula[i+1: j])
                #更新当前如果有数字
                for k, v in curr.items():
                    curr[k] *= cnt
                
                
                last = stack.pop()
                for k, v in last.items():
                    curr[k] = curr.get(k, 0) + last[k]
                
                i = j - 1 # why j - 1
            elif ord('A') <= ord(formula[i]) <= ord('Z'):
                j = i + 1
                while j < len(formula) and ord('a') <= ord(formula[j]) <= ord('z'):
                    j += 1
                ele = formula[i: j]
                i = j

                while j < len(formula) and formula[j].isdigit():
                    j += 1
                
                if j == i:
                    num = 1
                else:
                    num = int(formula[i:j])
                curr[ele] = curr.get(ele, 0) + num
                i = j - 1
                
                
                
            i += 1
            
        ans = ''
        for k, v in sorted(curr.items()):
            ans += k
            if v > 1:
                ans += str(v)
        return ans
        
        