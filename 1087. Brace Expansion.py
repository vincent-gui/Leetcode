题目 展开字符串

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

就是模板, 这里需要注意逗号需要用while 不停地backtrack

class Solution:
    def expand(self, s: str) -> List[str]:
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
        
        
        new = ''
        for item in s:
            if item.isalpha():
                new += '{' + item + '}'
            else:
                new += item
        s = '{' + new + '}'
        stack_op = []
        stack_str = []
        curr = []
        
        for i in range(len(s)):
            if s[i] == '{':
                stack_str.append(curr[:])
                stack_op.append(0)
                curr = []
            elif s[i] == ',':
                stack_str.append(curr[:])
                stack_op.append(1)
                curr = []
            elif s[i].isalpha():
                curr += [s[i]]
            elif s[i] == '}':
                while stack_op[-1] == 1:
                    curr = stack_str[-1] + curr
                    stack_op.pop()
                    stack_str.pop()
                if stack_op[-1] == 0:
                    curr = product(stack_str[-1], curr)
                    stack_op.pop()
                    stack_str.pop()
                
        return sorted(curr)