#总结, 这个是做的sliding window 的最后一个题, 一开始还考虑到需要用一个check{} 和一个int valid 去track 最后是否相当后来发现完全不需要那个valid, 因为必须是substring, 所以反而不需要valid 

#怎么样判断window 的长度, 用一个cnt 去track, 每次加入一个词,cnt += 1, 然后用这个cnt 去和len(words) 作比较, 不能和len(view) 作比较, 因为有可能出现相同的词

#什么时候需要valid 这个变量, window 里不仅仅有target letter or word 的时候, 需要valid, 典型题目 76


#思路, 以words 里单词的长度为最开始循环次数, 如果长度3, 那么就从0, 1, 2 作为大循环开始位置, 这个题不需要考虑最后单词够不够组成一个单词长度


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        loop = len(words[0])
        view = {}
        
        for word in words:
            view[word] = view.get(word, 0) + 1
           
        start = -1
        ans = []
        
        for i in range(loop): #大循环开始位置, 搜索 [0, 3, 6], 再搜[1, 4, 7], 最后搜[2, 5, 8]
            start = i
            check = {}
            cnt = 0
            for j in range(i, len(s), loop):
                word = s[j: j + loop]
                cnt += 1
                check[word] = check.get(word, 0) + 1
                if cnt > len(words):
                    cnt -= 1
                    t_word = s[start:start + loop]
                    start += loop
                    check[t_word] -= 1
                    if check[t_word] == 0:
                        del check[t_word]
                    
                
                if view == check:
                    ans.append(start)
        
        return ans