总结: sliding window 好像就是从头开始, 往window里放, 当小于window 长度的时候就添加, 如果大于就把最开始的start 移动一下(可能移动+1, 也可能移动到最右侧+1)

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = {}
        view = {}
        start = 0
        for i in range(len(p)):
            d[p[i]] = d.get(p[i], 0) + 1

        ans = []
        
        for i in range(len(s)):
            view[s[i]] = view.get(s[i], 0) + 1
            if i - start + 1 > len(p):
                view[s[start]] -= 1
                if view[s[start]] == 0:
                    del view[s[start]]
                start += 1
            if view == d:
                ans.append(start)
        
        return ans
                