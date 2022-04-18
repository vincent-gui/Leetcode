题目: 
	给一个二叉树, 要求按照从左到右把node 分组, 每组内, 从上到下, save level 的从小到大排序
	
解法: 正常从左到右就是 从0开始, left child 就-1, right child + 1, 同时用两个变量track, 最左和最右就可以了
但是这个题每个d[col] 里并不是单个的val, 而是(row, node.val), 这样按照col 遍历的时候, 需要把当前col 都整体排序, 就可以得到答案




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        d = {}
        queue.append((root, 0, 0)) #node, left/right, depth
        
        left = right = 0
        while queue:
            node, col, row = queue.popleft()
            left = min(left, col) #下次遇到从左到右, 记住用两个变量记录, 最左最右, 可以避免最后排序
            right = max(right, col)
            
            d[col] = d.get(col, []) + [(row, node.val)]
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        
        ans = []
        
        for col in range(left, right + 1):
            ans.append([item[1] for item in sorted(d[col])])
        
        return ans