题目: 给一个string, 和一堆词, 问 没能否从这这堆词中拼出string


解法就是dfs, dp ,每次选第一个, 两个, 直到发现第一个词在里面, 然后dfs 剩余的部分, 这个时间复杂度2**n, 加memo 后降低到n**3, 因为每个字母要循环, 这是O(n), 对于每个字母, 要循环n**2, 所以是N的3次


除了basic dfs, 剩余的时间复杂度都是N**3
#dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #f[i] 表示以第i个index 结尾的能否都在wordDict里
        f = [False] * (len(s) + 1)
        f[0] = True
        d = set(wordDict)
        
        for i in range(1, len(f)): #外层表示从左到右, 以第i个字母结尾的substr 是否在再dict里
            for j in range(i - 1, -1, -1):  #这里正推反推已经没有关系了, 因为第f[i-1] 已经计算过了
                if f[j] and s[j:i] in d:
                    f[i] = True
                    break
        
        return f[-1]

#DFS + MEMO
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return True
            out = False
            for i in range(len(s)):
                new_word = s[:i + 1]
                
                if new_word in d:
                    out = out or dfs(s[i + 1:])
                    if out is True:
                        return True
            memo[s] = out
            return out
        
        return dfs(s)



#DFS + MEMO
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        @lru_cache
        def dfs(s):
            if not s:
                return True
            out = False
            for i in range(len(s)):
                new_word = s[:i + 1]
                
                if new_word in d:
                    out = out or dfs(s[i + 1:])
                    if out is True:
                        return True
            return out
        
        return dfs(s)
		
		
#DFS		
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        def dfs(s):
            if not s:
                return True
            out = False
            for i in range(len(s)):
                new_word = s[:i + 1]
                
                if new_word in d:
                    out = out or dfs(s[i + 1:])
                    if out is True:
                        return True
            return out
        
        return dfs(s)