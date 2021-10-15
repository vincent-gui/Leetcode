解法: 

和前序类似, 不过post order 是倒过来的, 最后一个就是root 节点, 所以递归的时候也是先右后左

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(postorder.pop())
            node = TreeNode(inorder[idx])
            node.right =  self.buildTree(inorder[idx + 1:], postorder)
            node.left = self.buildTree(inorder[:idx], postorder)
            return node