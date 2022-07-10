题目: 猜单词, 给了一串单词, 问让最多猜10次, 猜到这个单词, 有一堆备选单词里猜 

 #没头绪
        
        #猜一个, 基于反馈, 变更到下一个词, 感觉向bfs, 一个词到另外一个词有几个度
        #肯定要对单词组本身做个preprocess
		#一开始觉得相似的至少相同的字母数量要越来越大, 后来发现并不是这样的, 因为越多未必就代表越相似, 所以只能用相等的保留
		
		
		
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def similarity(word1, word2):
            cnt = 0
            for char1, char2 in zip(word1, word2):
                if char1 == char2:
                    cnt += 1
            return cnt
        
        
        for i in range(10):
            tmp = []
            idx = randint(0, len(wordlist) - 1)
            match = master.guess(wordlist[idx])
            if match == 6:return
            for word in wordlist:
                if word == wordlist[idx]: continue
                if similarity(word, wordlist[idx]) == match: #这里必须是等号
                    tmp.append(word)
                    
            wordlist = tmp
        
        