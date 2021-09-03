思路:

两点, 但是两点一般是两个while 循环, 或者外层用for 顺序遍历, 内层用while 改变slow 指针的位置

这个题一开始的思路是slow 不懂, 计算cnt,然后直接把cnt 放进slow后面那个位置, 后来发现如果字母超过9个, 就需要两个位置, 这个时候其实可以灵活变通, 因为slow 位置固定, 那么把cnt 变成string, 然后循环这个cnt, 并且给slow 赋值, slow += 1

!!!!!
这里有个小trip, 因为如果最后一个字母有可能会直接跳出, 但是其实需要多出力一次, 所以外层循环多了一次, 但是内层首先判断i < len(chars), 这样不会越界, 还能处理最后一个字母

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        slow = 0
        cnt = 1
        
        for i in range(1, len(chars) + 1): #这里多跑一遍, 为了处理最后一个字母
            if i < len(chars) and chars[i] == chars[i - 1]:
                cnt += 1

            else:
                chars[slow] = chars[i - 1] #这里这个不能少, 因为如果前一个字母超过3个, slow 就还在前一个字母上
                slow += 1
                if cnt > 1:
                    for s in str(cnt): #这里处理的非常漂亮, 直接变成string 一个个往下循环更改就可以
                        chars[slow] = s
                        slow += 1
                    cnt = 1 #别忘记重置cnt
					
        
        return slow