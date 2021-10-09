前序 是 中左右, 后续是左右中, 所以把前序的进stack 的顺序反转一下就可以

class Solution(object):
    def postorderTraversal(self, root):
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
                curr = curr.right
                
            curr = stack.pop()
            curr = curr.left
        
        return ans[::-1]