
题目: 给一个数组, 和一个k, 问每次可以从头, 或者末尾选择一个数, 选k次,然后需要让选出来的这k 个数字的和最大

解法: 说白了就是一个循环数组, 中的substring 最小, 这样剩余的部分就最大

如果一共有10 个数字, 让选7个数字, 也就意味着剩余三个连续的数最小, 那么剩下7个就最大


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) <= k:
            return sum(cardPoints)
        
        left = len(cardPoints) - k
        sub_sum = sum(cardPoints[:left])
        ans = sub_sum
        
        for i in range(left, len(cardPoints)):
            sub_sum += cardPoints[i] - cardPoints[i - left]
            ans = min(ans, sub_sum)
        
        return sum(cardPoints) - ans