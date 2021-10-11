
解法1, dfs/recrusive 初始设置low upper as 最小最大

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, -sys.maxint, sys.maxint)
    
    
    
    def valid(self, node, low, upper):
        if node is None:
            return True
        if node.val <= low or node.val >= upper:
            return False
        
        return self.valid(node.left, low, node.val) and self.valid(node.right, node.val, upper)
		
		
		
解法2: BFS

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [(root, -sys.maxint, sys.maxint)]
        
        
        while queue:
            node, low, upper = queue.pop(0)
            if node.val <= low or node.val >= upper:
                return False
            
            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, upper))
        
        return True
        
解法3, 利用BST 的属性, inorder 的时候是递增排列

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        return self.dfs(root, ans)
        
    def dfs(self, node, ans):
        if not node:
            return True
        left = self.dfs(node.left, ans)
        
        if ans and ans[-1] >= node.val:
            return False
        ans.append(node.val)
        
        right = self.dfs(node.right, ans)
        
        return left and right'
		
		
解法4 inorder iter 方法 判断上一个数字是否大于等于node.val
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root, False)]
        num = None
        
        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    if num is not None and num >= node.val: 注意这里不是if num, 如果num 等于也会报错
                        return False
                    num = node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        
        return True