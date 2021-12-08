一开始的思路是贪心, 就是看那里能延伸到最大, 但是其实是错误的, 

正确的解法是哪个苹果快要过期就得先吃 

用一个heap 去保存, 保存的格式是(过期的日子, 剩余的苹果数)

为什么不用for loop 是因为即使没有苹果了, 但是还可以有没吃完的苹果, 
所以用了while i < size or heap

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        ans = 0
        i = 0
        size = len(apples)
        
        while i < size or heap:
            if i < size:
                heappush(heap, [i + days[i], apples[i]])
            while heap and (heap[0][0] <= i or heap[0][1] <= 0):
                heappop(heap)
            if heap:
                heap[0][1] -= 1
                ans += 1
            i += 1
        
        return ans