class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #这个题特殊情况就是 0 + 60 和30 + 30 这样的需要单独统计cnt[0], else 里包括了1~59
        cnt = defaultdict(int)
        ans = 0
        for t in time:
            if t % 60 == 0:
                ans += cnt[0]
            else:
                ans += cnt[60 - t % 60] # 1 ~ 59
            cnt[t % 60] += 1
        return ans