class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        out = node.val
        right_node = node.right
        while right_node:
            self.stack.append(right_node)
            right_node = right_node.left
        
        return out
        

    def hasNext(self) -> bool:
        return self.stack