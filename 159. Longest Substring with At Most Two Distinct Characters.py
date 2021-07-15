'''

总结:

这个题第一个思路就是用sliding window, 用一个dict 去存字母的index
注意!!! 每个字母只保存最大的index
不需要考虑新的字母是否在不在dict里

解法: 
每一个字母加入到dict里
	如果len(d) > k: 那么从d里找到idx 最小的那个字母, 剔除掉
	并且start = min(idx) + 1
ans = max(ans, 当前i - start + 1)

return ans

'''
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        d = {}
        
        for i, c in enumerate(s):
            d[c] = i
                
            if len(d) == 3:
                idx = len(s) + 1
                key = None
                for i1, v in d.items():
                    if v < idx:
                        idx = v
                        key = i1

                idx = min(d.values())
                left = idx + 1
                del d[key]
            ans = max(ans, i - left + 1)
        
        return ans


                
                
                
                    