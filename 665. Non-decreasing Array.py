题目: 非递减数列, 问给一个数列, 至多改变一个数字, 问可不可以变成非递减数列

# 1, 4, 2, 6
当检测到4, 2 的时候, 考虑将4变成2
  
# 3, 4, 2 ,6
当检测到4,2 的时候, 如果只是简单的把4, 变成2, 这个时候就意味最开始的3 也需要变化, 但是还可以将2 变成4

所以逻辑就是当遇到降低的, 同时检测i-1 这个值, 确保这个值<= i+1, 
这样就可以改变为nums[i] = nums[i+1], 否则就是第二种nums[i+1] = nums[i]




class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                changed = True
                if i:
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i + 1]
                    else:
                        nums[i + 1] = nums[i]
        return True