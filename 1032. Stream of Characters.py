解法: 利用trie 结构, 但是在这个题中会出现一些怪异的情况

比如 ['abc', 'bc'] 如果按照正常的顺序建立trie, 就没办法验证'bc' , 因为每一次streaming 的最后一个字母可以作为验证的标准, 

所以建立trie 的时候 , 将所有单词倒过来建立trie 就可判断

用一个deque 存储所有的已经出现的字母, 每一次从左向右扫描即可

时间复杂度为O(m) m 是trie 的深度

1. 标准写法

class TrieNode():
    def __init__(self):
        self.next = {}
        self.isString = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.queue = deque()
        self.curr_node = None
        for word in words:
            self.insert(word[::-1])
        
        
    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.next:
                curr.next[letter] = TrieNode()
            curr = curr.next[letter]
        curr.isString = True
        
    
    def query(self, letter: str) -> bool:
        curr = self.root
        self.queue.appendleft(letter)
        
        for letter in self.queue:
            if curr.isString:
                return True
            if letter not in curr.next:
                return False
            curr = curr.next[letter]
        
        return curr.isString
        
        
2. 简略写法

from collections import deque
class StreamChecker:

    def __init__(self, words):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie       
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word #在每个单词最后append 一个'$' 表示结尾了
        
        
    def query(self, letter) :
        self.stream.appendleft(letter)
        
        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node       


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)