
题目, 层级便利, 导出每层的最大值

就是tree 的level order trevasl, 如果没有就把第一个数放进去, 如果有, 就看看是不是需要更新


Time: O(n) 
space O(h) stack 的空间

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, depth):
            if not node:
                return 
            if depth >= len(ans):
                ans.append(node.val)
            else:
                if ans[depth] < node.val:
                    ans[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans