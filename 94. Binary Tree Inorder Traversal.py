class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
c.right = d

总结: 
1. 先将所有左子树放入stack, 用两个变量, curr 和stack track, 当curr 是None 的时候, 从stack pop, 这样就保证了最左边一定被最先pop 出来, 并且加进ans
2. 又因为 left node 同时也为middle node, 所以中在左之后, 最后一步就是让node = node.right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stack = [], []
        curr = root
        
        while curr or stack:
            while curr: #这步保证了所有left 都在第一步
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() #这一步保证了左 或者中, 先把val 放进ans
            ans.append(curr.val)
            curr = curr.right #再进行这一步, 保证了right 边所有的子树 都在中node 之后进入ans
        
        return ans
		
		
#非常棒的一个版本, 一套模版cover了三种order 写法

https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions