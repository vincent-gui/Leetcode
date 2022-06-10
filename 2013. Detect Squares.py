题目: 设计题
给了一个stream 流的数组, 问每次给一个点, 返回已经有的点可以组成多少个正方形

解法:, 给定的点为固定点, loop 现在的所有点作为对角线点, 就可以推导出四个点的坐标, 

最后用cnt * 点3 和点4 的数据量, 就是结果


class DetectSquares:

    def __init__(self):
        self.c = Counter()
        

    def add(self, point: List[int]) -> None:
        self.c[tuple(point)] += 1
        
        

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x, y), cnt in self.c.items():
            if x == x1 or abs(x - x1) != abs(y - y1):
                continue
            ans += cnt * self.c[(x, y1)] * self.c[(x1, y)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)