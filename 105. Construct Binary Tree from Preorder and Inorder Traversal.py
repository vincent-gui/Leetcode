解法

前序遍历的关键就是前序遍历第一个一定为root 节点, 用这个root 节点在中序遍历里找index, index左边为左子树所有的点, 右边为右子树所有的点
现在返回preorder, 第二个node, 就是inorder 左边的子树的root 节点, 递归求解


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            #pre order 的第一个点就是根节点, 找到inorder 的index, 左边就是左子树, 右边就是右子树
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx + 1:])
            return node 