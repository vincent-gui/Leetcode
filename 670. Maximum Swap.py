题目就是给一个非负数, 允许交换两个位置, 返回能够获得的最大数字

注意, 输入是一个int, 所以需要转化为数字数组

解法: 贪心
	遍历整个数组, 记录每个数字出现的最后的位置
	从左向右遍历数组, 内部从9倒着遍历到当前数字. 如果一旦发现位置比当前位置靠右, 交换并返回
	2996 -> 交换第二个9. 所以应该是9926

这个题写的不好, 命名乱七八糟
class Solution(object):
    def maximumSwap(self, nums):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(nums))
        position = [-1 for i in range(0, 10)]
        for i, num in enumerate(nums): #循环扫描一遍, 得到每个数字最后出现的位置
            position[int(num)] = i
            
        for i, num in enumerate(nums):
            for check in range(9, int(num), -1): #对于现在这个数字, 从9开始到当前数字, 如果位置比当前靠后, 交换
                if position[check] > i:
                    nums[i] = str(check)
                    nums[position[check]] = num
                    return int(''.join(nums))
        
        return int(''.join(nums))