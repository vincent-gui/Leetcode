题目: 给了一串单词, 问每次给这个单词最后添加一个字母, 能找到的最长的单词是什么
如果同时最长,那么返回字母顺序小的


方法1, brute force
time : 26*m*n, m 是数组的长度, n 是每个单词的长度

class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set(words)
        ans = ''
        for word in words:
            if len(word) < len(ans):
                continue
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix not in seen:
                    break
                if len(prefix) > len(ans):
                    ans = prefix
                elif len(prefix) == len(ans):
                    if prefix < ans:
                        ans = prefix
        return ans


方法2: trie + BFS #trie node 保存的是完整的单词

time : m*n, m 是数组的长度, n 是每个单词的长度

class TrieNode:
    def __init__(self,):
        self.child = defaultdict(TrieNode)
        self.word = None
        
    def insert(self, word):
        curr = self
        for letter in word:
            curr = curr.child[letter]
        curr.word = word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        ans = ''
        
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            for c in curr.child.values():
                if c.word != None:
                    if len(c.word) > len(ans) or (len(c.word) == len(ans) and c.word < ans):
                        ans = c.word
                    queue.append(c)
        
        return ans
		
		
#传统trie写法

from collections import defaultdict, deque
class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
    """
    @param: word: a word
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.word = word
       

class Solution:
    def longestWord(self, words) -> str:
        trieRoot = Trie()
        for word in words:
            trieRoot.addWord(word)
            
        ans = ""
        bfs = deque(trieRoot.root.children.values())
        while bfs:
            cur = bfs.popleft()
            for child in cur.children.values():
                if child.word != None:
                    if len(child.word) > len(ans) or len(child.word) == len(ans) and child.word < ans:
                        ans = child.word
                    bfs.append(child)
        return ans