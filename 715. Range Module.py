题目: 给一个数组, 添加区间, remove 区间, 检查区间是否在给的已有的范围内


这个题没啥说的, 背会就行
https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation

class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        l, r = bisect_left(self.intervals, left), bisect_right(self.intervals, right)
        
        tmp = []
        if l % 2 == 0:
            tmp.append(left)
        if r % 2 == 0:
            tmp.append(right)
        self.intervals[l:r] = tmp
        

    def queryRange(self, left: int, right: int) -> bool:
        l, r = bisect_right(self.intervals, left), bisect_left(self.intervals, right)
        return l == r and l % 2 == 1
        

    def removeRange(self, left: int, right: int) -> None:
        l, r = bisect_left(self.intervals, left), bisect_right(self.intervals, right)
        tmp = []
        
        if l % 2 == 1:
            tmp.append(left)
        if r % 2 == 1:
            tmp.append(right)
        self.intervals[l:r] = tmp
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)