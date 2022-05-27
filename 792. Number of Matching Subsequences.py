题目: 给一个字符串, 和一堆词, 问这堆词里有多少个, 是字符串的subsequence

Brute force 解法
对于每一个word, 做two point 扫描, 
time:  (m + n) * k 


二分解法
对于每个s 里的字母做预处理, 用一个hashmap 存储每个字母出现的idx, 因为对于每个字母, value 都是一个排好序的list, 然后做二分即可

二分过程: 从0开始, 第一个字母里找到, +1 就是下一个curr 的开始, 如果超过了当前字母的最大的index, 那么就是false
time : n*lgM*k


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(word):
            curr = 0
            for letter in word:
                idx = bisect_left(d[letter], curr)
                if idx >= len(d[letter]):
                    return False
                curr = d[letter][idx] + 1
            return True
        
        d = defaultdict(list)
        for i, letter in enumerate(s):
            d[letter].append(i)
        
        return sum([isSubseq(word) for word in words])