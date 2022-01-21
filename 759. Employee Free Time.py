最好还是用合并interval 的方式, 最后再得出结果
用下面的方法可能会造成出现[94, 94] 的情况, 比如[[[1,2],[2,3]],[[4,10]]]

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []
        
        events = []
        
        for times in schedule:
            for time in times:
                events.append([time.start, -1])
                events.append([time.end, 1])
        
        balance = 0
        events.sort()
        prev = None
        ans = []
        for time, eventType in events:
            if balance == 0 and prev is not None and prev != time: # 这里必须有这个条件prev != time, 否则会出现[2,2]
                ans.append(Interval(prev, time))
            
            balance += eventType
            if balance == 0:
                prev = time
        
        return ans