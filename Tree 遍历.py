#pre order

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], [(root, False)]
        
        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    ans.append(node.val)
                else:
                    #preOrder 中左右, 这里就是右左中
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        
        return ans
		
		
#in order

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], [(root, False)]
        
        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    ans.append(node.val)
                else:
                    #preOrder 中左右, 这里就是右左中
                    stack.append((node.right, False))
					stack.append((node, True))
                    stack.append((node.left, False))
        
        return ans
		
		
#post order

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], [(root, False)]
        
        while stack:
            node, seen = stack.pop()
            if node:
                if seen:
                    ans.append(node.val)
                else:
                    #preOrder 中左右, 这里就是右左中
					stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        
        return ans