KMP 没啥意思

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ''
        size = len(part)
        
        for letter in s:
            stack += letter
            if len(stack) >= size:
                if stack[-size:] == part:
                    stack = stack[:len(stack) - size]
        
        return stack