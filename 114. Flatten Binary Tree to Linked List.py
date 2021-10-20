这个题和430 题就是相同的题目, 没什么区别

解法1: 
dfs 一进来先让prev.right 指向当前
然后保存当前right, 把left node 丢进dfs, 返回则为tail, 返回完以后将node.left 设置为none, 再继续dfs(tail, tmp_right)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(-1)
        self.dfs(dummy, root)
        
        return dummy.right
        
        
    def dfs(self, prev, curr):
        if not curr:
            return prev
        prev.right = curr
        
        tmp_right = curr.right
        tail = self.dfs(curr, curr.left)
        curr.left = None
        return self.dfs(tail, tmp_right) #这一步太精华了
        
		
解法2, stack, 先放入right, 再放入left, 最后一步最重要
perv = curr	
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        dummy = prev = TreeNode(-1)
        stack = [root]
        
        while stack:
            curr = stack.pop()
            
            prev.right = curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                curr.left = None
            prev = curr
        
        return dummy.right