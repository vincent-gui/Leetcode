题目: 给了一堆时间, 求最小的分钟差

一开始想到了两点
        # 1. how to get mins difference , 用hour * 60 + min 解决
        # 2. how to get min difference, 排序解决
		
		还有一个问题就是timePoints = ["23:59","00:00", "00:03"], 答案应该是第一个时间和第二个时间组成, 但是如果我再比一次最后一个和第一个("23:59","00:00")就很丑
		t.append(t[0] + 1440)  就顺利的解决了这个问题
		

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 1. how to get mins difference
        # 2. how to get min difference
        t = sorted(int(time[:2]) * 60 + int(time[3:]) for time in timePoints)
        t.append(t[0] + 1440) # 为了check 第一个和最后一个, 确保不会是 ["23:59","00:00"] 这样的
        return min(b - a for a, b in zip(t, t[1:]))