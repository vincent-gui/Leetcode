题目, 对角线遍历, 但是每个row 的长度不一样

解法, 用 i+ j 去判断行列, 
创建一个ans = [], if len(ans) <= i + j:
就添加新的一列, 因为所有的数是按照从左到右放进去的, 最后需要从右到左搞出来


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        
        ans = []
        for i in range(n):
            for j in range(len(nums[i])):
                if i + j >= len(ans):
                    ans.append([])
                ans[i + j].append(nums[i][j])
                
        return [num for row in ans for num in row[::-1]]
		#这里, 正常是 [num for num in row[::-1] for row in matrix] 但是这样会报错, 所以需要把for num in row[::-1] 放在row 循环的后边