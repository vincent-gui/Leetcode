题目: 给一堆task, 然后一个冷却时间, 问最短需要总过多少时间完成所有的task


解法:
	找到最多的任务例如 AAABBBCCCDDE, N=2
	这个时候, 最高频率就是3, 
	也就意味这其实可以频出A..A..A
	
	下一步就是如果最高频率只出现一次, 那么..就可以把剩余所有的填进去(如果有一堆单独的任务超过了..数量除外)
	A.. 一共出现了几次, 2次, 其实是3个A 需要两个间隔, 每个间隔的距离是(n+1) 
	所以可以得出 (most_count - 1) * (n + 1), 但是如果出现aaabbbcc 的时候怎么办, 需要最后再加一个(有几个字母都是最高频率, 这里是3, 所以公式是  (most_count - 1) * (n + 1) + num_of_letter_with_most_count
	
	还有一种例外, 就是aaabbbcdef, 公式计算是 2 * (2 + 1) + 2 = 7, 但是任务都有10个, 所以最后返回还需要和len(tasks) 做个比较

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        c = Counter(tasks)
        most_task, cnt = c.most_common()[0]
        addOn = 0
        for k, v in c.items():
            if v == cnt:
                addOn += 1
                
        return max(((cnt -  1) * (n + 1) + addOn), len(tasks))