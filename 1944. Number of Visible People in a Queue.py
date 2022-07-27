题目. 给了一串数组, 代表每个小人的身高, 问每个小人向右看的时候, 能看到几个人
单调栈肯定的, 但是怎么做呢

一开始想到了对于每一个人, 看这个人后面一个人为起点的单调递增, 也就是倒着遍历的单调递减

比如
 [10,6,8,5,11,12]
 10开始, 那么是以6为起点, 12为终点的单调递增[6,8,11], 但是也需要注意, 10 是看不到12 的, 因为被11 挡住了, 
 
接着就考虑到那么倒序, 然后对于每一个mono_stack 做一个binary serarch, 可行的, 但是这个mono_stack 是个倒序, 最后需要转过来, 导致LTE

正确解法
上面一步不需要binary search, 每次退栈也就意味着这个被退掉的其实是可以被当前小人看到, cnt += 1
最后看看stack 是不是空, 不为空 就意味着还可以看到, 上例中, 10 最后会把 6 ,8,都推掉, 这会cnt = 2, 然后还需要+= 1, 因为还可以看到11


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            cnt = 0
            while stack and stack[-1] < heights[i]:
                cnt += 1
                stack.pop()
            if stack:
                cnt += 1
            stack.append(heights[i])
            ans.append(cnt)
        
        return ans[::-1]