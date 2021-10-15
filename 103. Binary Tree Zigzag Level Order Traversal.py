class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        is_even = 1
        ans = []
        
        while queue:
            level_list, size = deque(), len(queue)
            for _ in range(size):
                node = queue.popleft()
                if is_even:
                    level_list.append(node.val)
                else:
                    level_list.appendleft(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(level_list)
            level_list = deque()
            is_even = (is_even + 1) % 2
            
        return ans