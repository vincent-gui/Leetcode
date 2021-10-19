class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans, path = [], []
        self.dfs(root, ans, path, targetSum)
        
        return ans
        
        
    def dfs(self, node, ans, path, target):
        if not node:
            return 
        if node and not node.left and not node.right and target == node.val:
            ans.append(copy.deepcopy(path + [node.val]))
            return #注意这里的return, 有可能得到第一个结果的时候直接return 从而导致, 最后一个num 没有pop 掉
        self.dfs(node.left, ans, path + [node.val], target - node.val)
        self.dfs(node.right, ans, path + [node.val], target - node.val)