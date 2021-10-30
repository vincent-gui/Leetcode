解法1

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0



解法2 lgn * lgn , 这种解法 充分利用到满树的性质, 如果左右深度一样, 那么 返回左子树 + root 的个数(2**深度), + 右子树 的个数
如果左右不一样, 那么意味着 左子树最后一层都不满, 这时返回的就是右子树满树个数(2** right 深度) + 左子树个数

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        leftDepth = self.count(root.left)
        rightDepth = self.count(root.right)
        if leftDepth == rightDepth:
            return 2 ** leftDepth + self.countNodes(root.right)
        else:
            return 2 ** rightDepth + self.countNodes(root.left)
        
        
    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left)