这个题目的意思就是给了一个数组manager, idx 是员工, value 是manager id, 然后每个manager 通知所有属于他的员工时间也给出来了

一开始想的是用bfs 便利, 遇到了就加一次时间, 后来发现同一个manager 地下, 通知一次就可以
然后就想分层遍历应该可以, 结果还是错的, 因为有可能左孩子的和左孙子一起用的时间 还没有右孙子一个用的时间多

思路是从上倒下遍历, queue里维护了当前需要check 的node, 和到当前node 需要的时间, 每次遍历完更新一下全局ans

这个解答是建立在left node 的时间一定是0 的基础上
time compx 是O(n)
space 是O(n)


BFS

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):

        ans = 0
        neighbors = {i: [] for i in range(n)}
        for i in range(n):
            if manager[i] != -1:
                neighbors[manager[i]].append(i)
            
        queue = deque([(headID, 0)])
        while queue:
            id, time = queue.popleft()
            ans = max(ans, time)
            for neighbor in neighbors[id]:
                queue.append((neighbor, time + informTime[id]))
        
        return ans
		
DFS
这个dfs 解法相当精炼, 以后需要朝这个方向学习
	
class Solution(object):
    def numOfMinutes(self, n, headID, managers, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        neighbors = defaultdict(list)
        for i, manager in enumerate(managers):
            neighbors[manager].append(i)
        
        def dfs(id):
            ans = 0
            for neighbor in neighbors[id]:
                ans = max(ans, dfs(neighbor) + informTime[id])  #对于每一个child node , 都遍历一次, 并且更新最大值, 属于top down dfs
            return ans
        
        return dfs(headID)
		
		
bottom up DFS(牛逼解法)
	其实这里并不能完全算bottom up, 比较巧妙的是, 从任意一点出发, 只要不是root node , 就进一步dfs, 直到找到root node , 返回root node 的time
	这个时候会从上到下更新每个node的time(这个时间存储的就是从root node 到当前node 一共需要花多少时间, 并且把当前node 的父node 变成-1, 也就意味着每个node 只遍历一次, 下次直接可以从时间list 里获取, 类似于dp 的解法)

class Solution(object):
    def numOfMinutes(self, n, headID, managers, informTime):       
        def dfs(id):
            if managers[id] != -1:
                informTime[id] += dfs(managers[id])
                managers[id] = -1
            
            return informTime[id]
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans
        