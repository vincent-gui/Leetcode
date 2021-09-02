思路, 二元一次方程的性质, a >= 0,开口向上, 那么最大值一定就是第一个数和最后一个数中更大的

相反a<0, 最小的数一定是第一个数 和 最后一个数里相对小的那个数

用一个idx 去track (idx = 0 if a < 0 else len(nums) - 1), 如果a < 0, 则从左向右放入
a>=0, 从右向左放入

两点比较大小, 哪边放入, 移动哪边, 注意要让l<= r

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        idx = 0 if a < 0 else len(nums) - 1
        ans = [None] * len(nums)
        l, r = 0, len(nums) - 1
        def quadratic(num):
            return a * num ** 2 + b * num + c
        
        while l <= r: #两数相等的时候也需要计算一次, 否则最后一个数会漏掉
            l_num, r_num = quadratic(nums[l]), quadratic(nums[r])
            if a >= 0:
                if l_num > r_num:
                    ans[idx] = l_num
                    l += 1
                else:
                    ans[idx] = r_num
                    r -= 1
                idx -= 1
            else:
                if l_num< r_num:
                    ans[idx] = l_num
                    l += 1
                else:
                    ans[idx] = r_num
                    r -= 1
                idx += 1
        
        return ans
                
        