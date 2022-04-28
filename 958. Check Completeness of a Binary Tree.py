
解法1.  DFS, 利用完全二叉树的性质, left idx 是root idx * 2 , right 是 root idx * 2 + 1, 所以遍历所有node, 可以得到最大的node number和总node 的个数, 如果相等, 就是true

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, pos):
            if not node:
                return 
            self.mx_pos = max(self.mx_pos, pos)
            self.cnt += 1
            dfs(node.left, 2 * pos)
            dfs(node.right, 2 * pos + 1)
        
        self.mx_pos = 0
        self.cnt = 0
        dfs(root, 1)
        return self.mx_pos == self.cnt



解法2. BFS 层级便利, 如果有None在中间, 返回False
[1,2,3,4,5, None,None,None,None] True
[1,2,3,None,5, None,None,None,None] False

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        i = 0
        queue = [root]
        while queue[i]:
            queue.append(queue[i].left)
            queue.append(queue[i].right)
            i += 1
        
        return not any(queue[i:])