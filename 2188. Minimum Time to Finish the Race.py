题目: 给了一串数组, 代表最初轮胎时间[time, power] 例如[2, 3] 就以为跑第一圈用2分钟, 第二圈用2*3, 第三圈是2*(3**2)

给了个换轮胎的时间, 和圈数

问跑这么多算最少用多少时间

典型的DP


 开始想法      
# f[i] is the ith lap spend time
#f[i + 1] = min(f[i] using same tire , min others + 5) 错了!!! 以后要考虑如果不能i-1, 能不能i-j 项
#f[i][j] #meaning ith lap end with tire j

#after video
开完video 后
#f[i] = f[i - j] + switch time + min(j)



class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires.sort(key = lambda x: x[1])
        new_tire = []
        for tire in tires:
            if new_tire and new_tire[-1][0] <= tire[0]:
                continue
            new_tire.append(tire)
        print(new_tire)
        tires = new_tire
		#这一行以上是一个优化, 否则过不了, 按照power 排序, 从小到大, 如果power 大, 并且base 也比new_tire 里最后一项大, 就可以直接丢掉
		
        def getChangeTime(tires):
            minTime = [float('inf') for _ in range(numLaps + 1)]
            for i in range(1, numLaps + 1):
                for tire in tires:
                    first, q = tire[0], tire[1]
                    minTime[i] = min(minTime[i], first * (q ** i - 1 ) // (q - 1))
            
            return minTime
        
        minTime = getChangeTime(tires)
        print(minTime)
        
        f = [float('inf') for _ in range(numLaps + 1)]
        f[0] = 0
        for i in range(numLaps + 1):
            for j in range(1, i + 1):
                f[i] = min(f[i], f[i - j] + minTime[j] + (changeTime if i > j else 0))
        
        return f[-1]
        
        