题目: 
给一串开始结果的ts, 计算每个任务总共用多久

思路:
	前提条件只能是相对应的nest
	
	第一反应是stack, 但是stack 里存什么呢, 是idx 和 ts吗???
	
	知道的是 每一次遇到end status,  需要给结果 + 1, 但是 如果prev  是5, end 是6, 再+1 就不适用了, 
	其实这里prev 总是track 的是一个新的时间段的开始的数字, 所以每次遇到end, prev 也需要+ 1
	
	再看就是start status, 换另外一个start 计算结果是直接相减就可以了
	
解法: stack 里只存idx, 不存ts, ts 由变量prev 保存




class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []

        
        for log in logs:
            idx, status, ts = log.split(':')
            idx, ts = int(idx), int(ts)
        
            if status == 'start':
                if stack:
                    ans[stack[-1]] += ts - prev_time
                stack.append(idx)
                prev_time = ts
            else:
                ans[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1
        return ans