
题目: 最小矩形面积, 给一堆点, 问能否用这堆点拼出最小的矩形, 且面积最小, 不可以拼就返回0

思路, 循环对角线的两个点 (x1, y1), (x2, y2), 那么剩下两个点的坐标就是  (x1, y2), (x2, y1)
只需要遍历对角线的两个点,然后判定剩余两个点是否在set 里就可以

点不重复的模板写法 

for x1, y1 in points:
	for x2, y2 in seen:
		#do something
	seen.add((x1, y1))

还有一种优化解法; 复习的时候再看
https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        ans = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
            seen.add((x1, y1))
        
        return ans if ans !=  float('inf') else 0