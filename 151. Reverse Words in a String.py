方法1  

string 变成全部的单字母list 用 list(string)
string 变成全部的单字母list且去重 用 set(string)

先变list, 全部反转
将里面的词反转: 同向双指针, l = r = 0, r < len(arr), 只要r 等于space, 那么调用上一步 reverse_string 
移除首尾space: 每个条件都需要保证 l < r 
移除内部space: 

def trim_space(self, word):
        if not word:
            return []
        
        ans = [word[0]]
        
        for i in range(1, len(word)):
            if ans[-1] == ' ' and word[i] == ' ':
                continue
            ans.append(word[i])
        
        return ans



class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        self.reverse_string(arr, 0, len(arr) - 1)
        self.reverse_word(arr)
        word = self.trim_side(arr)
        ans = self.trim_space(word)
        
        return ''.join(ans)
        
        
    def trim_space(self, word):
        if not word:
            return []
        
        ans = [word[0]]
        
        for i in range(1, len(word)):
            if ans[-1] == ' ' and word[i] == ' ':
                continue
            ans.append(word[i])
        
        return ans
        
        
        
    def trim_side(self, arr):
        l, r = 0, len(arr) - 1
        while l < r and arr[l] == ' ':  #这里只需要l < r, 不需要 l <= r
            l += 1
        while l < r and arr[r] == ' ': #这里只需要l < r, 不需要 r >= 0
            r-= 1
        return arr[l: r + 1]
        
        
    def reverse_word(self, arr):
        l, r = 0, 0
        
        while r < len(arr):
            while r < len(arr) and arr[r] != ' ':
                r += 1
            self.reverse_string(arr, l, r-1) #注意这里是r-1, 因为r 其实是不符合的
            r += 1
            l = r
        
    def reverse_string(self, arr, start, end):

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1; end -= 1
        
        




方法2

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1]).strip()