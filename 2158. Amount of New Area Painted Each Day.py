题目: 给了一串tuple, (start,end) 代表在start 和end 之间刷油漆, 并且同一个区间油漆不能刷多次

Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1.



解法1: 类似于跳表的一个数据结构对于每一个中间值都存储end 的idx
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 4] 以后会变成
[0, 4, 4, 4, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


[4, 7] 以后会变成
[0, 4, 4, 4, 7, 7, 7, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[5,8] 因为idx = 5 的位置上已经不是0了, 就直接得到idx = 5 那个的值, 7, 7就是需要开始的新的idx, 因为7 是0, 所以从7 开始到8. 记1

class Solution:
    def amountPainted(self, paint) :
        records = [0] * 50000
        
        ans = []
        
        for start, end in paint:
            tmp = 0
            while start < end:
                if records[start] != 0:
                    start = records[start]
                else:
                    tmp += 1
                    records[start] = end
                    start += 1
            ans.append(tmp)
        
        return ans
paint = [[1,4],[4,7],[5,8]]
Solution().amountPainted(paint)




解法2: 维护了一个sorted containers
思路就是对于每一个开始结束, 用扫描线
对于每一个start或者end, 都维持一个(start/end, idx, flag)

然后当如果一个pos 有多个idx 的时候
比如 [[1,4],[4,7],[5,8]]
	 [  0,     1,   2  ]
pos 4 这个点有两个[(4, 0, -1), (4, 1, 1)] 这个里也维持的有序的
如果flag== 1, 那么idx 加入sorted set, 如果-1 , 就移除, 每次sorted [0] 号为+= 下一个的pos


from sortedcontainers import SortedDict, SortedSet
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        records = SortedDict()
        
        for i, (start, end) in enumerate(paint):
            records[start] = records.get(start, []) + [(i, 1)]
            records[end] = records.get(end, []) + [(i, -1)]
        s = SortedSet()
        ans = [0] * len(paint)
        array = [ (k, records[k]) for k in records.keys()]
        for i in range(len(array)):
            pos = array[i][0]
            for idx, flag in array[i][1]:
                if flag == 1:
                    s.add(idx)
                else:
                    s.remove(idx)
            
            if i + 1< len(array) and s:
                ans[s[0]] += array[i + 1][0] - pos
                
        return ans