有一串任务, 每个人物有两个属性(attack, defense), 人物是弱批的定义是但凡有任意一个别的人两个属性都碾压当前这个弱批, 则弱批+= 1

返回几个弱批

同俄罗斯套娃, 能套几个, 被套的都是弱批


解题方法: (attack, defense) 先按照attack 排序, 如果attack 相同的按照defense 排序  
这个时候attack 就会变成严格的不一样, 一样的都排在一起了. 遍历defense

单调递减栈, 如果比stack[-1] 小或者等于, 就说明可以放入递减栈, 如果严格大于, 就把栈里比当前defense 小的都弹出, 并且每次弹出ans += 1(因为弹出了弱批). 最后返回ans


class Solution(object):
    def numberOfWeakCharacters(self, nums):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        nums = sorted(nums, key = lambda x: (x[0], -x[1]))
        stack = [] #monotonic stack >
        
        ans = 0
        for attack , defence in nums:
            while stack and stack[-1] < defence:
                ans += 1
                stack.pop()
            stack.append(defence)
        
        return ans