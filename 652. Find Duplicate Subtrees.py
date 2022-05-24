题目: 给了一个tree, 要求返回所有的相同的子树

传统做法就是对于每个node 和子node进行serial, 然后以这个为key放入hashmap里, 如果key 出现初则value + 1. 如果第一次看到value == 2, 就放入结果

时间复杂度 N**2 , 解释一下, 遍历所有node 需要O(n), 但是对于每一个node 建立hashkey, 其实还需要遍历一下, 这里又是一个O(n).

解法1: 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:
                return '#'
            key = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right) #不加',' 会导致 1, 11, 和 11, 1 变成valid 的结果
            d[key] += 1
            if d[key] == 2: #只添加一次
                self.ans.append(node)
            return key
        
        d = defaultdict(int)
        self.ans = []
        dfs(root)
        
        return self.ans
		
		

解法2, hash of hash, 就是返回的就是hash 值, 然后基于这个再次做 hash, 也不需要加分割node 的',', 因为是hash of hash

time: O(n)
space: O(n)

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node):
            if not node:
                return '#'
            key = str(hash(str(node.val) + dfs(node.left) + dfs(node.right)))
            d[key].append(node)
            return key
        
        d = defaultdict(list)
        dfs(root)
        
        return [nodes.pop() for nodes in d.values() if len(nodes) >= 2]