当两个单词相同的时候, 只需要让p1, p2 轮流等于idx 就可以求出最小!!!

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        size = len(wordsDict)
        
        p1 = p2 = -size
        ans = sys.maxsize
        same = word1 == word2
        for i in range(size):
            if wordsDict[i] == word1:
                p1 = i
                ans = min(ans, p1 - p2)
                if same:
                    p2 = p1
            elif wordsDict[i] == word2:
                p2 = i
                ans = min(ans, p2 - p1)
                
        return ans 