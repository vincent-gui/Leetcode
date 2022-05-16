题目: 给了一堆山峰高度, 山峰之间可以存水, 问可以的存多少水

解法 1: 
1. 从左向右 保存一个单调递增数列
2. 从右向左 保存一个单调递增数列 

用min(left[i], right[size - i - 1]) - height[i] 就可以得到当前位置能够存储多少水



time : O(n)
space: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        
        for h in height:
            if not left or left[-1] < h:
                left.append(h)
            else:
                left.append(left[-1])
        
        for h in height[::-1]:
            if not right or right[-1] < h:
                right.append(h)
            else:
                right.append(right[-1])
        
        ans = []
        size = len(height)
        print(left)
        print(right)
        for i in range(size):
            ans.append(min(left[i], right[size - i - 1]) - height[i])
        
		
解法 2: 

用left, right保存左侧最大, 和右侧最大
然后比较哪一层更小, 就意味着在整个区间的标准是当前这个mark, 如果heigh[i] 比这个mark 小, 就给ans 添加, 否则更新mark

time: O(n)
space: O(1)





        return sum(ans)