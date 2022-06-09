题目 给了一个list 包括了(开始时间, 运行时间) 要求根据下面的要求
返回执行顺序

1. 如果cpu IDLE, cpu 保持IDLE
2. CPU 会选择开始时间最早的job 运行
3.  如果两个job 开始时间相同, 则选择运行时间短的执行
4. cpu 可以结果同一个task 立刻开始下一个task


一开始确实想到了priorityQueue 但是困惑在怎么去track curr Time 和运行时间, 是否需要每次+= 1

解法: 先用(开始时间, 运行时间, 和idx 排序), 因为最后需要idx 输出

	整体的frame 就是每次都添加任务进入queue, 然后 用currTime = max(currTime, task[0]) 更新currTime
		内部就是如果curr 小于当前task 的时间, 并且priority queue 不空, 就取出, 然后让curr 的时间+ 运行时间
	
	最后如果queue 还有东西, 因为curr 一直track 的是开始时间, 也就意味着queue里一定包括了所有未运行的任务, 继续process 就行
	
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return []
        ans = []
        tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        currTime = 0
        heap = []
        
        for task in tasks:
            while currTime < task[0] and heap: #为什么是小于???  因为并不知道后一个task 是不是和curr 的time 相等, 如果相等, 一定要把所有当前等于curr 的都放进queue里, 才能从queue 里pop 出来, 所以只能是小于
                runTime, idx = heapq.heappop(heap)
                ans.append(idx)
                currTime += runTime
            heapq.heappush(heap, (task[1], task[2]))
            currTime = max(currTime, task[0])
        
        while heap:
            runTime, idx = heapq.heappop(heap)
            ans.append(idx)
            #currTime += runTime
        
        return ans