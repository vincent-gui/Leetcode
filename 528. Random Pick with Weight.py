题目: 给一个数组, 按照每个数字占的比例 随即给出所属于的index, 比如 [1, 3], 
那么每次抽取, 取index 0 的概率是25%, 取index 1 的概率是75%

解法: 给数字做一个prefix sum, 注意这里没有初始0 在第一位. 所以prefix [1, 4]
做二分, total 是4, 用函数random.random 取得一个0~ 1 之间的数, 然后这个数就是target, 做二分.

最后判定条件就是start <= target, return start, 否则就是end


class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])
        self.total = self.prefix[-1]
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        start, end = 0, len(self.prefix) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if self.prefix[mid] <= target: #因为是prefix sum, 没有重复数字
                start = mid
            elif self.prefix[mid] > target:
                end = mid
                
        if self.prefix[start] >= target: #需要检测是因为[1,3,4,2] -> [1, 4, 8, 10], 有可能会出现小于1的target
            return start
        return end
                