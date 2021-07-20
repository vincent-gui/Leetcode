总结:
最开始的思路是一个sliding window, 但是考虑到每次dict 里存的是index, 每次需要再检索 dict


07/20 
在sliding window里, start 不能回撤!!!
例如tabbcderft, 这个题在遇到两个b 的时候, start 已经指向第二个b, 但是遇到最后一个t的时候, 如果不加限制, 因为d[t] 为0, 所以start 会退回到1的位置,这是错误的!!!


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        07/20
        """
        
        d = {}
        
        ans = start = 0
        
        for i, letter in enumerate(s):
            if letter in d:
                prev_idx = d[letter]
                start = max(prev_idx + 1, start)
            d[letter] = i
            ans = max(i - start + 1, ans)
        
        return ans
                










07/13
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