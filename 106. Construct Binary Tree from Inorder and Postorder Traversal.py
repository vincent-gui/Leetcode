解法: 

前序遍历的关键就是前序遍历第一个一定为root 节点, 用这个root 节点在中序遍历里找index, index左边为左子树所有的点, 右边为右子树所有的点
现在返回preorder, 第二个node, 就是inorder 左边的子树的root 节点, 递归求解

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