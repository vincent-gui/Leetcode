
题目 : 一个string, 里面有一些字母, 然后查询如果有连续k个, 就pop


解法: 用stack 存, 不过每个node 表示了字母和个数
time N


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for letter in s:
            if not stack or stack[-1][0] != letter:
                stack.append([letter, 1]) # 这里是精华, 第一次遇到保存[leetter, count]
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k: #如果等于k 了, 就pop 
                    stack.pop()
        
        return ''.join([item[0] * item[1] for item in stack])