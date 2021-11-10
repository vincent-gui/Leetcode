方法1:
inOrder + findKth , 注意findKth模版需要记住

time:O(n) + lg(n) + O(k)
space: O(n)


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nums = self.dfs(root)
        return self.findK(nums, target, k)
        
        
    def dfs(self, node):
        if not node:
            return []
        return self.dfs(node.left) + [node.val] + self.dfs(node.right)
        
        
        
    def findK(self, nums, target, k):
        ans = []
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        while k > 0:
            left_diff = abs(nums[start] - target) if start >= 0 else float("inf")
            right_diff = abs(nums[end] - target) if end < len(nums) else float("inf")

            if left_diff < right_diff:
                ans.append(nums[start])
                start -= 1
            else:
                ans.append(nums[end])
                end += 1
            k -= 1
        
        return ans
		
		
解法2: 骚操作
时间O(lgH) + O(k), 扫描
空间O(h), 包括get stack 从上到下

1.先遍历数组, 同时建立两个stack prev & nxt , 如果node < target, 那么prev.append(node), node = node.right 否则nxt.append(node), node = node.left
2. 这样会得到两个被压缩的stack, 然后分别pop, 比较哪个更近
3. 将tree 中别的数放进相应的stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ans = []
        if root is None or k == 0:
            return ans
        
        prev, nxt = self.find_stack(root, target)
        
        for _ in range(k):
            left_diff = abs(prev[-1].val - target) if prev else float("inf")
            right_diff = abs(nxt[-1].val - target) if nxt else float("inf")
            if left_diff < right_diff:
                ans.append(self.get_left(prev))
            else:
                ans.append(self.get_right(nxt))
                
        return ans
                
    def get_left(self, prev):
        node = prev.pop()
        nxt_node = node.left
        while nxt_node:
            prev.append(nxt_node)
            nxt_node = nxt_node.right
        
        return node.val
    
    def get_right(self, nxt):
        node = nxt.pop()
        nxt_node = node.right
        while nxt_node:
            nxt.append(nxt_node)
            nxt_node = nxt_node.left
        
        return node.val
                
        
    def find_stack(self, node, target):
        prev, nxt = [], []
        
        while node:
            if node.val < target:
                prev.append(node)
                node = node.right
            else:
                nxt.append(node)
                node = node.left
        
        return prev, nxt
    
            