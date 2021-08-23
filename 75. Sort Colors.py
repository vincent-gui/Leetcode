解法2:

建立首尾双指针left和right，分别指示0/1边界和1/2边界。left左边（不含left）全为0，right右边（不含right）全为2。初始化left和mid为0，right 为len(nums)-1。
第三个指针mid从left起向right移动，边扫描边实时更新两个边界。
若 nums[mid]为 0 ：交换第 mid个和第left个元素，并将 left 指针和mid指针都向右移。
若 nums[mid]为 2 ：交换第 mid个和第 right个元素，并将 right指针左移
若 nums[mid]为 1 ：将指针mid右移。
补充一下，当mid与left交换后，mid能够后移，因为此时nums[mid]可能为0，后面还需要与left交换

三个注意:
1. idx <= right, 因为有可能right 还没有被检查
2. left 交换后, left 和 idx 都需要+= 1, 原因如下
3. right 交换后, 只移动right, 因为idx 这个数是新的数字,还没有check 过



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = idx = 0
        right = len(nums) - 1
        
        while idx <= right:
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1 
                idx += 1 #为什么这里又需要+= 1, 而不会像下面那个出现数没检查, 是因为idx 左边都已经是被扫描过得, 也就是说只会出现[0, 0, 1,1,0] 这样的情况, 而不会出现2 
            elif nums[idx] == 2:
                nums[right], nums[idx] = nums[idx], nums[right]
                #!!!!!idx += 1 不能idx += 1, 因为换过来的这个数没有检查过
                right -= 1
            elif nums[idx] == 1:
                idx += 1
        

解法1: 统计多少个数字, 然后赋值
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        d[0], d[1], d[2] = 0, 0, 0
        
        for num in nums:
            d[num] += 1
        
        for i in range(len(nums)):
            if d[0] > 0:
                nums[i] = 0
                d[0] -= 1
            elif d[1] > 0:
                nums[i] = 1
                d[1] -= 1
            else:
                nums[i] = 2
                d[2] -= 1