题目: 一个二叉树, root 为0, 左子树为2*value + 1, 右子树为 2*value + 2

恢复这颗二叉树, 然后查看是否有target 的值

follow up , 如果node过多, 造成set 装不下怎么办???

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.seen = set()
        def dfs(new, node):
            if not node:
                return 
            node.val = new
            self.seen.add(new)
            dfs(new * 2 + 1, node.left)
            dfs(new * 2 + 2, node.right)
        dfs(0, root)
        
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen