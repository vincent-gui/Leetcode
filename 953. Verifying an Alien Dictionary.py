class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i, letter in enumerate(order):
            d[letter] = i
        
        words = [[d[letter] for letter in word] for word in words]
        for w1, w2 in zip(words, words[1:]):
            if w1 > w2: #这里比较的是数组 [1,2,3] > [1,2]
                return False
        
        return True