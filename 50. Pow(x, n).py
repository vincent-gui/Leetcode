题目: 实现x 的n 次方

思路: 2 的10 次 就是 2 的5次 * 2 的五次
那么就可以用记忆化 这个属于开始top down, 计算的时候bottom up

如果用while 循环, 则一开始就是bottom up

time: lgN
space: lgN


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        power = self.myPow(x, n / 2)
        if n % 2 == 0:
            return power * power
        else:
            return power * power * x
			
	
time: lgN
space: 1	
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        
        ans = 1
        while n > 0:
            if n % 2 != 0: #一开始好奇什么时候ans被x复制, 其实每一次ans 被*x 都是把多余的一个 当前的x 放进ans 里, 最后n 等于1
			 的时候, 全部放进去
                ans *= x
            x *= x
            n /= 2
        
        return ans
		
		
2 ** 10 就意味着 4 ** 5, 因为这个5 是奇数, ans *= 4, 变成 4 * (4**4), -> 4 * (16 ** 2)

2(10) = (2 ** 2) ** 5
