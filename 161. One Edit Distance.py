解法1:  insert和delete 是同一个效果


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        if abs(m - n) > 1:
            return False
        if m == n:
            return self.check_same(s, t) 
        if m > n:
            return self.check_insert(t, s)
        else:
            return self.check_insert(s, t)
   
    def check_insert(self, t, s):
        i = j = 0 #同向双指针
        flag = False
        while i < len(t):
            if t[i] != s[j]:
                if flag:
                    return False
                flag = True
                i -= 1
            i += 1
            j += 1
        
        return True
            
    
    def check_same(self, s, t):
		#注意这里 'c' 和'c'需要返回false
        cnt = 0
        
        for i in range(len(s)):
            if s[i] != t[i]:
                cnt += 1
        return cnt == 1


解法2

耍流氓版
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False 
        if not s and not t:
            return False
        
        minLen = min(len(s), len(t))
        
        for i in range(minLen):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:] or s[i:] == t[i + 1:]
            
        return abs(len(s) - len(t)) == 1 #'c' 与 'c' 需要返回False