bottom up 解法

解法1

初次自己的解法
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        dummy = TreeNode(-1)
        dummy.left = root
        node = self.dfs(dummy, root)
        root.right = None #没有这个不行, 会出现环
        
        return node 
                
        '''
        初次思路就是去到最左侧node, 然后倒着循环, 但是怎么样处理right node 呢
        应该是用dfs
        '''
        
    def dfs(self, prev, curr):
        #因为需要track 上一个node , 所以有一个prev
        if not curr:
            return prev
        
        #需要向左递归
        out = self.dfs(curr, curr.left)
        curr.right = prev
        curr.left = prev.right

        
        return out
		
解法2 更简洁

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        
        left = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return left
		
		
解法3, top down


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
b.left = d
b.right = e

class Solution:
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        rootLeft, rootRight = root.left, root.right
        root.left = None
        root.right = None
        return self.topDown(rootLeft, root, rootRight)
    
    def topDown(self, rootLeft, root, rootRight):
        if not rootLeft:
            return root
        rootLeftLeft, rootLeftRight = rootLeft.left, rootLeft.right #这个方法就是先将当前点的左右存起来, 再将left 重置了, 然后用存着的left right 继续递归(1 改造, 进入2, 2进入后存好4, 5 再改造2, 改造完用45 继续递归
        rootLeft.left = rootRight
        rootLeft.right = root
        
        return self.topDown(rootLeftLeft, rootLeft, rootLeftRight)
        
Solution().upsideDownBinaryTree(a)