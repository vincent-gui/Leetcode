总结
两个dict 只存 需要的字母
多一个valid 变量去track 是否满足了所有的t

思路就是fast 指针快速向前, 一旦满足了t以后, slow 指针向前+1, 收缩整体长度, 每收缩一次更新一下最短长度与起始位置



class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        
        view = {}
        start = left = 0
        miLen = len(s) + 1
        valid = 0
        
        for i in range(len(t)):
            view[t[i]] = view.get(t[i], 0) + 1   
        d = {}
        
        for i, c in enumerate(s):
            if c in view:
                d[c] = d.get(c, 0) + 1
                if d[c] == view[c]: #这里需要考虑一下, 为什么不是>=, 因为等于就够了, 大于会使valid 数字不断增加
                    valid += 1
            
            while valid == len(view):
                if i - left + 1 < miLen:
                    miLen = i - left + 1
                    start = left
                letter = s[left]
                left += 1
                if letter in d:
                    d[letter] -= 1
                    if d[letter] < view[letter]: #这里需要考虑一下, 一旦小于就表示不够, 如果大于就忽略
                        valid -= 1
                
                
        
        return '' if miLen == len(s) + 1 else s[start: start + miLen]
    
    
                
                