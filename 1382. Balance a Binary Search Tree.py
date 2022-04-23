题目: 给一个非平衡的bst, 返回(数值相等, 全新的平衡bst), 平衡的定义是: 任何一个node 的左子树深度 - 右子树深度的绝对值不超过1

解法, inorder get 所有的node value, 二分build 新的bst

注意, 二分的时候, 跳出条件是 l > r: return None



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
a =  TreeNode(1)
b =  TreeNode(2)
c =  TreeNode(3)
d =  TreeNode(4)

a.right = b
b.right = c
c.right =d 


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
            
        def build(i, j):
            if i > j:
                return None
            mid = (i + j) // 2
            root = TreeNode(nodes[mid])
            root.left = build(i, mid - 1)
            root.right = build(mid + 1, j)
            return root
            
        dfs(root)
        return build(0, len(nodes) - 1)

Solution().balanceBST(a)