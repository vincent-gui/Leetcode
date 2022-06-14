
题目 略坑, 描述略坑
说白了就是给了一个数组, 偶数位是出现的次数, 基数位是数字, 给了一个next function,问每次call next 以后, 返回的数字是什么

例如[8,8,8,5,5] 给的数组就是[3,8,2,5] 三个8, 两个5

["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]

n = 2, 返回8, 也就是idx 等于1 的时候
n = 1, 返回8, 也就是idx 等于2 的时候
n = 1, 返回5(第一个5), 也就是idx 等于3 的时候
n = 2, 返回-1(超过了数组长度), 也就是idx 等于5 的时候

解法: 用一个idx 去只track 偶数位的数字 O(n)
还可以有binary search 的方法

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.nums = encoding
        self.idx = 0
        

    def next(self, n: int) -> int:
        
        while self.idx < len(self.nums) and self.nums[self.idx] < n: # why not == n
            n -= self.nums[self.idx]
            self.idx += 2
        
        if self.idx >= len(self.nums):
            return -1
        self.nums[self.idx] -= n
        return self.nums[self.idx + 1]
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)