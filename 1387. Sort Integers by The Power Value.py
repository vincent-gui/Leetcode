
题目: 给了一堆数, 根据下面这个规则, 定义num 需要几步变成1, 然后按照这个count 作为排序条件
	if x is even then x = x / 2
	if x is odd then x = 3 * x + 1
就是find kth 的变种, 

from sortedcontainers import SortedList
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        sl = SortedList()
        
        def getPowerValue(num):
            cnt = 0
            while num != 1:
                cnt += 1
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
            
            return cnt
        
        for num in range(lo, hi + 1):
            sl.add((getPowerValue(num), num))
        
        return sl[k - 1][1]#这里别忘了point 出来是第二项
        