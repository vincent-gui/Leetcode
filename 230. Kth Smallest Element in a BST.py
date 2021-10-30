#总结，利用inorder trversl 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        
        while root:
            stack.append(root)
            root = root.left
            
        while stack:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            right_node = node.right
            while right_node:
                stack.append(right_node)
                right_node = right_node.left