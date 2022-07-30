题目: 给一个字符串, 和一堆词, 问这堆词里有多少个, 是字符串的subsequence

Brute force 解法
对于每一个word, 做two point 扫描, 
time:  (m + n) * k 
s = "abcde", words = ["a","bb","acd","ace"]

二分解法
对于每个s 里的字母做预处理, 用一个hashmap 存储每个字母出现的idx, 因为对于每个字母, value 都是一个排好序的list, 然后做二分即可

二分过程: 从0开始, 第一个字母里找到, +1 就是下一个curr 的开始, 如果超过了当前字母的最大的index, 那么就是false
time : n*lgM*k

例子
abcbdbe
a:[0]
b:[1, 3, 5]
c:[2]
d:[4]
e:[6]

curr是从零开始, 用这个curr 去和每一个单调的做二分, 然后那个位置的数d[letter][new_idx] 就是当前这个字母在原始s 里的idx , 再+1就行



class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(word):
            curr = 0
            for letter in word:
                idx = bisect_left(d[letter], curr)
                if idx >= len(d[letter]):
                    return False
                curr = d[letter][idx] + 1 #这里为什么要+1, 因为如果是bb, 这个时候第一个curr 为0, 在[1] 这里搜索第一个b 会找到idx = 1, 这样如果+1, 就是2, 也就至少之后还得有一个b 的idx 大于等于2 , 否则就错
				但是如果不+1, 第一个找到以后将1 这个值赋予curr, 在用1 去[1] 里找, 找到的还是0, 是错误的
            return True
        
        d = defaultdict(list)
        for i, letter in enumerate(s):
            d[letter].append(i)
        
        return sum([isSubseq(word) for word in words])