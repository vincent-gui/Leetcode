   
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
		贪心
        """
        mx = 0
        
        for idx, num in enumerate(nums):
            if idx > mx:
                return False
            mx = max(mx, idx + num)
        
        return True
    

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        f[i] 表示能否跳到石头i
        f[i] = f[j] is True amd f[j] + A[j] >= i
        
        """
        
        n = len(nums)
        f = [False for _ in range(n)]
        f[0] = True
        
        for i in range(1, n): #从1开始判断
            for j in range(i): #枚举前0 ~ i项
                if f[j] and j + nums[j] >= i:
                    f[i] = True
                    break
        
        return f[-1]
        
