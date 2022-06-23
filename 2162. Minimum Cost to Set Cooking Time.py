题目: 最少之间设置cooking time, 从这个题可以看出来google 的人是闲的没事做
设置微波炉时间, hit buttom 有cost, switch 手指有cost, 问怎样设置给定的时间cost 更小

给定600秒, 可以设置成 10:00 分钟, 也可以设置成9分60秒, 
给76秒, 可以设置成1分16秒, 或者76秒

有几个edge case 需要考虑
6000秒是100 分钟, 但是分钟最大可以设置到99分钟, 秒也可以到99,
所以系统可以运行最大秒是 99 *60 +99 =6039, 但是这个case 不能用100:00 去计算cost, 因为mins 不能超过99

解法: 一个单独的func, 输入是分钟和秒, 然后转化成string 转化9分钟60秒的时候用的是 9 * 100 + 60 = str(960)
然后loop 就可以

主函数就是从最大min-1 开始loop 到最大min, 然后验证secs 是否超过99, 或者min 超过99, min 超过99 主要是为了防止 tagret > 6000的case, 只能用 99:xx秒表示, 不能表示为100:xx秒



class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            s, curr, ans = str(mins * 100 + secs), str(startAt), 0
            
            for ch in s:
                if ch == curr:
                    ans += pushCost
                else:
                    ans += (pushCost + moveCost)
                curr = ch
            return ans
        
        maxMins, ans = targetSeconds // 60, float('inf')
        
        for mins in range(maxMins - 1, maxMins + 1):
            secs = targetSeconds - mins * 60
            if secs > 99 or mins > 99:
                continue
            ans = min(cost(mins, secs), ans)
        return ans