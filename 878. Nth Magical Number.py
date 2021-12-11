
#  https://www.cnblogs.com/grandyang/p/11148889.html

公式 a/num + b / num - num/最小公倍数(a,b)


最小公倍数(a,b) = a * b / 最大公约数

二分答案, 这里要注意, num 选择的范围最小是2 , 最大是N 个 min(a,b) , 意味着至少有n 个解相对于a,b 


class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        mod = 10**9 + 7
        
        def lcm(a, b):
            while b: a, b = b, a % b
            return a
        gcd = a * b / lcm(a, b)
        
        start, end = 1,n * min(a, b)
        
        while start + 1 < end:
            mid = (start + end) / 2
            if mid / a + mid / b - mid / gcd < n:
                start = mid
            else:
                end = mid
                
        if start / a + start / b - start / gcd == n:
            return start % mod
        return end % mod