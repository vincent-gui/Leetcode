题目:  design 一个查询word 的, 但是有 ".", 一个"."表示一个字母

解法就是正常的trie, 但是遇到"." 就需要遍历当前层所有的子结点


class TrieNode:
    def __init__(self,):
        self.next = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.next:
                node.next[letter] = TrieNode()
            node = node.next[letter]
        node.isWord = True
        
        

    def search(self, word: str) -> bool:
        
        def dfs(word, node):
            for i, letter in enumerate(word):
                if letter in node.next:
                    node = node.next[letter]
                else:
                    if letter != '.':
                        return False
                    for child in node.next:
                        if dfs(word[i+1:], node.next[child]):
                            return True
                    return False
            return node.isWord
        return dfs(word, self.root)
                
        