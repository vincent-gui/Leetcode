题目: 在matrix 里找那些词出现过

一开始的思路就是对于每一个(i,j) 做dfs, 然后看看有没有可以组成 words 里的词, 但是如果words 很大, 每次对words 循环一次吗就很费时间了, 这个时候就考虑到trie 结构

但是如果只是朴素dfs 还是会超时, 因为对于一个全部都是a 的matrix, 即使所有的word 都找了,words 里已经没有了, 但是其实dfs 还是不会停下, 会继续扫描a 开始的trie , 太费时间, 需要特殊处理,


注意点:

1 找到一个isword 是true 的, 不可以return, 而是需要继续, 因为可能会有 'a' 和'aa' 两个都是答案
2. 这个题很经典的dfs 写法, 需要注意是现将答案添加进ans 里, 还是先验证i, j 是否invalid, 这里需要先添加答案, 因为如果整个matrix 只有一个元素, 先验证就会直接return了
3. dfs 的地方, 能否只有一个地方记录memo
	
	'''
	board[i][j] = '#'
    dfs(node.next[letter], i + 1, j, path + letter, ans)
    board[i][j] = letter
	
	'''
因为如果在主函数里也写一次, 有些面试官会觉得你有重复code(这个就很傻逼)

4. trie node 可以写成 
	self.next= defaultdict(trienode)
	节省时间

import collections

class TrieNode:
    def __init__(self, ):
        self.next = {}
        self.isWord = False
        self.cnt = 0
        
        
class Trie:
    def __init__(self,):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = TrieNode()
                node = node.next[letter]
            node.cnt += 1
        node.isWord = True
        

class Solution:
    def findWords(self, board, words) :
        ans = []
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
            
        def remove(word):
            node = self.trie.root
            for letter in word:
                node = node.next[letter]
                node.cnt -= 1
                
        def dfs(node, i, j, path, ans):
            
            if node.isWord:
                ans.append(path[:])
                remove(path[:])
                node.isWord = False
			if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 
            if node != self.trie.root and node.cnt == 0:
                return
            letter = board[i][j]
            if letter not in node.next:
                return 
            
            board[i][j] = '#'
            dfs(node.next[letter], i + 1, j, path + letter, ans)
            dfs(node.next[letter], i - 1, j, path + letter, ans)
            dfs(node.next[letter], i, j + 1, path + letter, ans)
            dfs(node.next[letter], i, j - 1, path + letter, ans)
            board[i][j] = letter
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(self.trie.root, i, j, '', ans)  
        
        return ans
            
            

board = [["a"]]
words = ['a']
Solution().findWords(board, words)