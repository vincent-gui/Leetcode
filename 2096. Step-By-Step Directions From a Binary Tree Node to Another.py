
题目: 给一个二叉树, 给一个start 节点和一个end 节点, 求他们之间的路径


思路就是
	如果左边是5->2->6 右边是5->2->4, source 是6, target 是4, 其实输出结果是要左边的从6开始逆序全部变成U, 右边是从上到下
	所以最接近不同的node(这里是2)之后的部分可以left + right
	
	或者先找到公共祖先, 用公共祖先开始左右分别找到source 和target, 然后相加就可以
	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, nums, target):
            if not node:
                return False
            if node.val == target:
                return True
            if node.left:
                path.append('L')
                nums.append(node.left.val)
                if dfs(node.left, path, nums, target):
                    return True
                path.pop()
                nums.pop()
            if node.right:
                path.append('R')
                nums.append(node.right.val)
                if dfs(node.right, path, nums, target):
                    return True
                path.pop()
                nums.pop()
            return False
            
                
            
        
        l_path, r_path, l_num, r_num = [], [], [], []
        dfs(root, l_path, l_num, startValue)
        dfs(root, r_path, r_num, destValue)
        
        i = 0
        while i < len(l_num) and i < len(r_num) and l_num[i] == r_num[i]:
            i += 1
        
        return (len(l_path) - i) * 'U' + ''.join(r_path[i:])














解法2 BFS, 用dict track [parent, leftKid, rightKid] 

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        neighbors = dict()
        
        def dfs(node, prev):
            if not node:
                return None
            neighbors[node.val] = [prev, node.left, node.right]
            dfs(node.left, node)
            dfs(node.right, node)
        
        prev = None
        seen = set()
        mapping = ['U', 'L', 'R']
        dfs(root, prev)
        seen.add(startValue)
        queue = deque()
        queue.append((startValue, ''))
        while queue:
                curr, step = queue.popleft()
                if curr == destValue:
                    return step
                neighbor = neighbors[curr]
                #是否需要seen
                for i in range(len(neighbor)):
                    if neighbor[i] != None and neighbor[i].val not in seen:
                        queue.append((neighbor[i].val, step + mapping[i]))
                        seen.add(neighbor[i].val)
                