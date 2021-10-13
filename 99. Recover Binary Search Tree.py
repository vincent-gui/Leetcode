总结, inorder 遍历bst 就是递增数列, 所以中序遍历的时候, 至多会遇到两次prev > node 的情况
因为是大的node 放在了小的tree 里, 所以第一次遇到的时候, prev 就是要找的那个大node, 第二次遇到的时候, node 就是要找的那个小node



解法1 recrusive
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, TreeNode(-sys.maxint)
        
        
        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev.val > node.val:
                    self.first = self.first or self.prev
                    self.second = node
                self.prev = node
                inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


解法2, iter	
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = [(root, False)]
        self.first, self.second, self.prev = None, None, TreeNode(-sys.maxint)
        
        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    if self.prev.val > node.val:
                        self.first = self.first or self.prev
                        self.second = node
                    self.prev = node
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        
        self.first.val, self.second.val = self.second.val, self.first.val
                
        