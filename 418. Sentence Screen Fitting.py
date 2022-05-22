题目: 给了一堆词, 然后给了一组长和宽, 问这一组词在所给的长和宽里能够完全重复几次

第一想法就是模拟吧, track 当前到哪个词了, 加上下个词是否超过宽度限制, 没有继续

代码如下, 这个最native 的解法中间被注释掉的部分就是问题, 如果每个词的长度是1, 但是rows 和cols 都很大. 例如20000

这个时候就很麻烦, 因为会在中间注释掉的部分循环两万次, 然后进入到下一个row, 再循环20000次
最后时间复杂度就是 rows * cols. 那么有没有更好地方法呢

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        idx = 0
        ans = 0
        for _ in range(rows):
            c = 0
            '''
            while c + len(sentence[idx]) <= cols:
                c += len(sentence[idx]) + 1 
                idx += 1
                if idx == len(sentence):
                    ans += 1
                    idx = 0
					
			'''
        return ans



肯定有, 反复看几遍以后发现, 因为每一个新的行都会以sentence 里的一个单词作为起始, 所以我们只需要记录下遇到的当前单词为开始的(返回为 以当前单词开始, 填满一行后, 下一行的第一个单词的idx, 和当前行被填满后, 整个词组可以被循环几次) 两个变量作为返回

比如
sentence = ["i","had","apple","pie"]
rows = 4
cols = 5

dp[0] 表示从单词 'i' 开始, 宽度为5 的, 返回就是 (2, 0) , 2 表示下一行开始的单词是apple 的idx, 0表示整个sentence 循环了0次

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        ans = 0
        wordIdx = 0 #track next word index
        
        @lru_cache(None)
        def dp(i): # i is current index in sentence we will use
            c = 0
            times = 0
            
            while c + len(sentence[i]) <= cols:
                c += 1 + len(sentence[i])
                i += 1 #move to next word
                if i == len(sentence):
                    i = 0
                    times += 1
            return i, times
        
        for _ in range(rows):
            ans += dp(wordIdx)[1]
            wordIdx = dp(wordIdx)[0]
            
        return ans
        