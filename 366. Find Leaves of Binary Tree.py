思路: 所有的leaf 节点的depth 就是0, 那么也就是none 节点为-1, 然后每个节点的depth , 由 depth = 1 + max(left_depth, right_depth) 去判定, 这样就能一层层把最外面的剥掉

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.dfs(root, ans)
        
        return ans
        
        
    def dfs(self, node, ans):
        if not node:
            return -1
        left_depth = self.dfs(node.left, ans)
        right_depth = self.dfs(node.right, ans)
        
        depth = 1 + max(left_depth, right_depth)
        if depth == len(ans):
            ans.append([node.val])
        else:
            ans[depth].append(node.val)
        return depth