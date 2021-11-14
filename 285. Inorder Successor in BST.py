解法1 中序遍历的后继节点

如果该节点有 右subtree, 那么后继节点就是right subtree 的最左端的节点
如果该节点没有 rigft subTree , 那么离该节点最近的父节点, 就是后继节点


如果p>=现在的root的话，那p的后继承一定是在整个右子树（因为inorder的顺序就是“左中右”) 相反，如果p<现在的root的话，那他的下一项有两个可能 1)如果left子树是空的话，那只有一个可能就是p的root 2)如果left子树不是空的话，答案就在整个左子树里 并且在recursion里面也已经考虑了p的右子树

iter 写法

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        
        while root:
            if root.val > p.val: #利用到的bst 的特性, root node 一定在left node 之后, 为什么不可以是等号呢
                successor = root
                root = root.left
            else:
                root = root.right
        
        return successor 
		
		
解法2, 递归

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if root.val <= p.val: #如果需要进入右子树, 起始等于从右子树重新搜索, 如果进入左子树, 那么记录当前的successor, 并且递归, 如果left 是空, 那么也就意味着左边没有找到successor, 这个时候需要return root,因为root 就是最近的parent
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        if left is None:
            return root
        else:
            return left