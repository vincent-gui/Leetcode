将每次词的index 都存成数组, 然后同时遍历, 辗转相减

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = {}
        
        for i, word in enumerate(wordsDict):
            self.d[word] = self.d.get(word, []) + [i]
        

    def shortest(self, word1: str, word2: str) -> int:
        arr1 = self.d[word1]
        arr2 = self.d[word2]
        
        i = j = 0
        ans = sys.maxsize
        while i < len(arr1) and j < len(arr2):  #这里就是辗转相减求最小
            idx1 = arr1[i]; idx2 = arr2[j]
            if idx1 < idx2:
                ans = min(ans, idx2 - idx1)
                i += 1
            else:
                ans = min(ans, idx1 - idx2)
                j += 1
        
        return ans
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)