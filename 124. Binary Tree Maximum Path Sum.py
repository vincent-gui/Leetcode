思路: 思路很直接, 左右两侧返回, 然后一个全局变量track 是否left + right + node.val > self.ans

但是返回需要返回 max(left, right) + node.val , 与0 的更大值

03/24
这个题和那个最长的tree 还是有区别的, 而且精妙的地方在于更新最大和return 分开, return那个地方要和0 作比较, 类似于dp 的一种方法

下面几个问题需要问清楚
1. node 有没有负数?
2. 会不会dfs 深度爆栈
3. 如果换成最长上升或者下降怎么处理






class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        self.dfs(root)
        
        return self.ans
        
        
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left + right + node.val > self.ans:
            self.ans = left + right + node.val
        
        return max(max(left, right) + node.val, 0)