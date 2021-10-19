#注意这里没有单独定义一个pathSum , 直接用targetSum -= node.val 就可以了

class Solution(object): 
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        targetSum -= root.val
        
        if root and not root.left and not root.right and targetSum == 0:
            return True
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)