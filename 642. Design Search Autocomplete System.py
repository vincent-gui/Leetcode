题目: 实现auto complete
大意: 给了一对句子, 给了次数, 然后问每次输入一个字母, 返回前三的句子是什么

用trie build 

search 需要用dfs



class Trie:
    def __init__(self,):
        self.isEnd = False
        self.cnt = 0
        self.next = {}


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.searchTerm = ''
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])
        
    def insert(self, sentence, cnt):
        node = self.root
        for var in sentence:
            if var not in node.next:
                node.next[var] = Trie()
            node = node.next[var]
        node.isEnd = True
        node.cnt -= cnt #注意这里是减等, 如果同一个句子被call 了两次, 那么计数应该是累加的效果
        
    def search(self,):
        
        def dfs(node, path):
            if node.isEnd:
                ans.append((node.cnt, path[:]))
            for var in node.next:
                dfs(node.next[var], path + var)
            
            
        node = self.root
        ans = []
        path = ''
        
        for var in self.searchTerm: #先遍历共有的, 当把当前的都遍历完 也就是 'I a' 都扫完了, 剩余部分需要dfs 自由发挥
            if var not in node.next:
                return ans
            path += var
            node = node.next[var]
        
        dfs(node, path)
        print(ans)
        return [item[1] for item in sorted(ans)[:3]]
        
        
        

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.searchTerm += c
            return self.search() 
        else:
            self.insert(self.searchTerm, 1)
            self.searchTerm = ''


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)