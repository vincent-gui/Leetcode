#大数乘法 就是每一位相乘, 向前错, i * j 的结果应该放在 i+j, i+j+1 这两个位置上, 从左到右为基准


	43
   *56
------
	18
   24
  15
 20
------
 21758
 


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1, s2 = len(num1), len(num2) #乘法的最后位数max 就是len(num1) + len(num2)
        
        ans = [0] * (s1 + s2)
        
        for i in range(s1-1,-1,-1): #倒序
            for j in range(s2-1,-1,-1):   #倒序
			#这里没有办法用divmod(int(num1[i]) * int(num2[j]), 10), 因为会出现相加以后超过10 的情况
			#先计算ans[i + j + 1]
                ans[i + j + 1] += int(num1[i]) * int(num2[j])
                ans[i + j] += ans[i + j + 1] /10
                ans[i + j + 1] %= 10
        ans = ''.join(str(char) for char in ans)
        
        return ans.lstrip('0') or '0' #注意去除向导0