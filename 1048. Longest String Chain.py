题目: 给了一些string, 如果一个string 增加一个letter 可以变成另外一个, 那么cnt 可以+1, 问最长的word chain 是多长

一开始想法是dfs, 时间复杂度是???

dp/Memo

解法1
bottom up , 对words排序, 这样从最短的单词开始 如果少一个字母在dict里, 那么+= 1

words = sorted(words, key = lambda word: len(word))
time: nlgn + n * L *L (排序 nlgn, 对于每一个单词(n), 内部都是LL(loop 单词, 基于每个位置, 创建新的substring) 


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = lambda word: len(word))
        d = {}
        ans = 0
        
        for word in words:
            curr = 1
            for i in range(len(word)):
                if word[:i] + word[i + 1:] in d:
                    curr = max(curr, d[word[:i] + word[i + 1:]] + 1)
            d[word] = curr
            ans = max(d[word], ans)
        
        return ans
		

解法2
top down, 这个就是记忆化, 无所谓从最长还是最短开始, 因为标准就是给定的words, 只有substirng 在这个words 才会继续
time : n * L *L
因为不需要排序	
	
from functools import lru_cache
class Solution:
    def longestStrChain(self, words) -> int:
        wordSet = set(words)
        memo = {}

        def dp(word):
            if word in memo:
                return memo[word]
            ans = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in wordSet:
                    ans = max(ans, dp(predecessor) + 1)
            
            memo[word] = ans
            return ans

        return max(dp(w) for w in words)

words = ["bdca","a","b","ba","bca","bda"]
Solution().longestStrChain(words)