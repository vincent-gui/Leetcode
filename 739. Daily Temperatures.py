
题目,. 给一串温度, 求当前天几天以后的温度比当前天的温度高

解法: 单调栈, 栈空或者和栈的最后一个小于等于当前温度, 入栈, 如果大于-1 的温度,则循环直到小于等于 当前温度为止, 更新循环的idx




#注意, 还有一个space O(1) 的解法,
https://leetcode.com/problems/daily-temperatures/discuss/397728/Easy-Python-O(n)-time-O(1)-extra-space-beat-99.9 


The idea is that going from right to left can reduce ton of repetitive work. We keep updating a variable right_max to store the current maximal number we have seen so far to the right of T[i] (not including T[i] itself).

If T[i] >= right_max, well, no future temperature will be strictly larger than T[i], so we simply update right_max = T[i] and move on to T[i-1].
If T[i] < right_max, we know there is a future warmer temperature, so we start our search. First compare T[i] with T[i+1], if T[i+1] is larger, we are done. Otherwise, we need to go further to the right. But by how far? Since we already did the search for T[i+1] before, we know that we need to go at least res[i+1] steps from T[i+1] to surpass T[i+1]. If T[i+1+res[i+1]] is larger than T[i], we stop; otherwise, we check the next larger number... We keep on doing this until we finally reach some number which is strictly larger than T[i].

Time O(n)
space O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        right_max = -float('inf')
        
        for i in range(len(temperatures) -1, -1, -1):
            t = temperatures[i]
            if t >= right_max: #why =, 因为等于也意味着没有需要更新的, 直接跳过就好
                right_max = t
            else:
                days = 1
                while temperatures[i + days] <= t: #如果向后extend 还是小于当前天的温度, 那么至少向后扩 ans[i+days] 天, 有点Dp 的意思
                    days += ans[i + days]
                ans[i] = days 
        
        return ans

Time O(n)
space O(N)

#思路: 单调递减栈, 从左到右, 如果当前小于(等于)栈最后一个元素, 入栈, 如果大于, 就回溯到把所有比当前小的都pop 出来后,了再把这个当前入栈

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] >= temp:
                stack.append((temp, i))
            else:
                while stack and stack[-1][0] < temp: #栈里最后一个元素小于当前
                    prev_temp, idx = stack.pop()
                    ans[idx] = i - idx
                stack.append((temp, i))
        
        return ans

简化为下面的code

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((temp, i))
        
        return ans
                