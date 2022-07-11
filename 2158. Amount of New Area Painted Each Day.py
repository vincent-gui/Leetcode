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