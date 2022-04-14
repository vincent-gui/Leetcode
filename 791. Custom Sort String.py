题目: 给了一个order string 作为标准顺序, 给了一个s 作为被检测string. 要求按照标准顺序排序被检测string

解法: 用一个dict 统计每个字母出现的次数, 然后遍历标准string, 从counter 里得到次数, 
	最后把counter 里剩余的append 到最后
	
	time : O(s) + O(t), 需要遍历order string 和 被检测string
	space O(26)
	

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        counter = {}
        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1
        
        ans = ''
        for letter in order:
            if letter in counter:
                ans += letter * counter[letter]
                del counter[letter]
        
        for k in counter:
            ans += k * counter[k]
            
        return ans
		