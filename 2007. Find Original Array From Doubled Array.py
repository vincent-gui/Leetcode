题目: 给了一个数组, 该数组是由original 的数组里的每一个数乘以2, 后append 到original 数组形成的(乱序)
问原数组是什么

限制, 每一个数字大于等于0 , 很关键!!!

解法: 对数组做排序去重

0 的个数如果不是偶数, 则不行
c[num] 的个数如果大于c[num*2] 的个数也不行
c[num*2] -= c[num]

最后返回剩余的部分

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        if c[0] % 2:
            return []
        for num in sorted(c): #注意这里是排序且去重的数字
            if c[num] > c[num * 2]:
                return []
            c[num * 2] -= c[num] if num else c[num] // 2
        return list(c.elements()) #element 会把小于1 的数组都忽略