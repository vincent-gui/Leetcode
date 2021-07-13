总结:
最开始的思路是一个sliding window, 但是考虑到每次dict 里存的是index, 每次需要再检索 dict

解法:
if 遇到新字符, 都存入dict里, 并且更新mx

else 如果遇到已经存过的(并且需要将viewed[c] 和 start 指针相比较, 因为其实不能小于start, 如果小于start 就意味着出现了a...m m ......a, start 已经在第二个m了, 但是viewed['a'] 还在第一个位置, 这个时候, 就需要更新mx, 而不是更新start), 将start 指针指向前一个位置 + 1

最后要更新viewed[c] = 当前i


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        start, mx = 0, 0
        viewed = {}
        
        for i, c in enumerate(s):
            if c in viewed and start <= viewed[c]:
                start = viewed[c] + 1
            else:
                mx = max(mx, i - start + 1)
            
            viewed[c] = i
        
        return mx