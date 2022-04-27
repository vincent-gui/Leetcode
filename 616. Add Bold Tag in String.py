题目: 给一个字符串, 给一个词组数组, 要求凡是出现在数组的词组, 都要加粗<b></b>, 就是添加这个东西

思路: 一开始一点思路也没有, 后来看答案, 意思就是其实可以用一个bool 的数组去track 每一个字母, 如果True 就说明要加粗 

https://leetcode.com/problems/add-bold-tag-in-string/discuss/1035897/Python-both-version-(Trie-%2B-Merged-Intervals)-and-(Trie-%2B-mask)

主要考查点还是怎么去得到哪些字母需要加粗, 最容易想到的就是两层循环, 这样每次得到一个新的时候, 就可以去loop word, 如果word startswith 新的substring, 那么 mark[i: i+len(word)] = [True] * len(word)

 但其实这里可以用trie 做优化, 如果words 词组很大

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        mark = [False] * len(s)
        
        for i in range(len(s)):
            new_s = s[i:]
            for word in words:
                if new_s.startswith(word):
                    mark[i:i + len(word)] = [True] * len(word)
        
        ans = []
        
        for i, char in enumerate(s): #写法注意, 这里先检查是否要加粗
            if mark[i] and (i == 0 or mark[i - 1] is False):
                ans.append('<b>')
            ans.append(s[i]) #添加字母
            if mark[i] and (i == len(s) - 1 or mark[i + 1] is False): #判断是否要添加 关闭符号
                ans.append('</b>')
        
        return ''.join(ans)