题目: 给一个词组和一个词组加数字, 判定相应的数字跳过字母后, 两个是否相等


解法: two pointer, 先比较当当前是否相等, 相同继续, 不相同看看是不是数字, 如果是则 i += num, 不是返回false, 

最后一定要判定i == len(word) and j == len(abbr) , 比如例子 'a' 与 '2' 就应该返回false, 因为2直接超过了最后

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() and abbr[j] != '0': # 注意如果遇到的第一个就是0, 则返回false
                start = j
                while j < len(abbr) and abbr[j].isdigit(): #这里注意判定j 要小于len(abbr)
                    j += 1
                num = int(abbr[start : j])
                i += num
            else:
                return False
        return i == len(word) and j == len(abbr)
                