题目(!!! tree 就是graph!!!!) , 要求给一个tree, 然后按照到所有里target node 距离等于k 的点

解法: 关键点在于, 每个点并不知道他的parent node 是什么, 所以其实需要一个数据结构, 直到当前node 的parent node 就够了
这里用到了dict, key 就是node, val 就是parent node,

然后从target node 还是bfs, 如果但凡碰到第一个的step == k, 那么这一层所有的点都应该是答案

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i

from collections import deque
class Solution:
    def distanceK(self, root, target, k) :
        parent = {}
        def dfs(node, p = None): #记住这个写法, 可以连接当前node 和parent node 的关系
            if node:
                parent[node] = p
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = deque()
        queue.append((target, 0))
        seen = set([target])
        
        while queue:
            size = len(queue)
            if queue[0][1] == k: #这里需要先check 每一层是否已经到达k step
                return [item[0].val for item in queue]
            for _ in range(size):
                curr, step = queue.popleft()
                for nei in (curr.left, curr.right, parent[curr]):
                    if nei and nei not in seen:
                        queue.append((nei, step + 1))
                        seen.add(nei)
        return []
root = a; target = b; k = 2        
Solution().distanceK( root, target, k)