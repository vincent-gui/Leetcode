
解法1:
#深度作为ans 的index
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.dfs(root, ans, 0)
        
        return ans
        
        
    def dfs(self, node, ans, level):
        if node:
            if level == len(ans):
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            self.dfs(node.left, ans, level + 1)
            self.dfs(node.right, ans, level + 1)
        
        
        
解法2:
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root]) #注意这里用了deque 而不是queue.pop(0), 时间复杂度是O(n)
        ans = []
        
        while queue:
            curr_level, size = [], len(queue) #这里小技巧， 用size 固定pop 出几个
            for _ in range(size): 
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(curr_level[:])
        return ans
        
