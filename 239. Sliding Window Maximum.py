
题目: 
	一个数组, 给一个window, 返回window 里最大值
	
	两种解法, sliding window + 红黑树
	
	第二种 单调queue


import sortedcontainers
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = sortedcontainers.SortedList()

        slow = 0
        ans = []
        
        for i, num in enumerate(nums):
            sl.add((num))
            if i - slow + 1 > k:
                sl.remove(nums[slow])
                slow += 1
            if len(sl) == k:
                ans.append(sl[-1])
        
        return ans
		
		
		
		
单调queue 这个解法还是需要记录一下

	[3, -1, -3] 如果这个时候来了一个2, 那么我们其实知道, 在未来的几个range 里, -1, -3 都不可能是返回值, 因为2 比他们大
	所以用queue 维护一个单调递减的, 然后每个item 里存的是num, 和idx 的tuple , 每次先检测queue[-1] 是否比curr num 小, 
	然后检测queue[0] 的idx 与queue[-1] 的idx 相距是否超过了k个元素
	
	最后添加答案
		
		
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() #(save num, i) 
		
        ans = []
        for i, num in enumerate(nums):
            while queue and queue[-1][0] < num:
                queue.pop()
            queue.append((num, i))
            
            if queue[-1][1] - queue[0][1] + 1 > k: #这一步检查必须在append ans 之前做, 否则[1, -1], 1 会出现问题
                queue.popleft()
            if i + 1 >= k: #这里的更新
                ans.append(queue[0][0])
        
        return ans