一开始想一边循环, 每次000 的数量越多, 超过现有的就更新ans,
后来发先开头, 结尾 和中间需要分开计算
开头结尾 就是k, 有几个0, 就是几
中间部分的0000, 是零的个数+ 1 // 2


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = seats.index(1) #计算开始
        ans = max(ans, seats[::-1].index(1)) #计算结尾
        i = 0
        for j in range(len(seats)): #计算中间
            if seats[j]:
                ans = max(ans, j - i + 1 >> 1)
                i = j + 1
        return ans