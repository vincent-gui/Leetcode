解法:

这个题的意思是 把数字变成string, 求第n位
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18]

一位数
1~9 = 9 digit
两位数
10~99 = 90 * 2 = 180 digits
三位数
100~999 = 900 * 3 = 2700 digits

legth = [1, 2, 3, 4....]
start 是去寻找那个每个位数的起始值(1, 10, 100, 1000...)

假设n = 12

经过一轮, 
n 变成 3, n - 1 = 2, 这时候的2 是说n剩余两个digit, 而我们需要找到最开始n 属于的那个actual 数字, 用start += (n-1) / 2, 就找了 11
这时候因为找到了11, 那么接着需要知道, 是11 的第几位, n-1 % 2 可以知道是第几个digit




class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 9
        length = 1
        start = 1
        
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        start += (n - 1) / length
        return int(str(start)[(n - 1) % length])