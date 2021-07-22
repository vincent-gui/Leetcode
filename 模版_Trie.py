class TrieNode():
    def __init__(self):
        self.next = {}
        self.isString = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        curr = self.root
        for letter in word:
            if letter not in curr.next:
                curr.next[letter] = TrieNode()
            curr = curr.next[letter]
        curr.isString = True
        

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        if len(word) == 0 or word is None:
            return False
        curr = self.root
        
        for letter in word:
            if letter not in curr.next:
                return False
            curr = curr.next[letter]
        return curr.isString

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        if prefix is None or len(prefix) == 0:
            return False
        curr = self.root
        for letter in prefix:
            if letter not in curr.next:
                return False
            curr = curr.next[letter]
            
        return True
