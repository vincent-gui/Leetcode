解法1 stack + iter 的方法
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return ans


解法二: recrusive 的方法
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.preOrder(root, ans)
        
        return ans
        
    def preOrder(self, node, ans):
        if not node:
            return 
        ans.append(node.val)
        self.preOrder(node.left, ans)
        self.preOrder(node.right, ans)


解法3

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], []
        curr = root
        
        while curr or stack:
            while curr:
                ans.append(curr.val)
                stack.append(curr) #必须先放进stack 里, 再让他变成左子node
                curr = curr.left 
            curr = stack.pop()
            curr = curr.right
        
        return ans
