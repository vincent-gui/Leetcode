class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([root])
        ans = []
        
        while queue:
            curr_level, size = [], len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            ans.append(curr_level)
            curr_level = []
        
        return ans[::-1]