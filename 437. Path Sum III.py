要求是从上到下, 每一个节点和子节点组成sum 都可以计算一次

难点就在于, 怎么从每个节点开始重新计算, 如果这样, 每个节点, 和他的子节点都会被反复计算



解法思想就是利用prefix sum,  同题目 560. Subarray Sum Equals K
[1,2,3], tagret = 3, 那么记录prefixsum
[1, 3, 6], 也就意味着在 6 的时候, 减去3, 等于3, 如果3 出现在前面的prefix 里, 也就意味着前面有一堆数的和等于3

特别注意
1. d[0]=1, 这个是一个必须要注意的, 是为了应对[3], target = 3 这个情况
2. 主要每个点要回朔

内部顺序是
1. 先计算cumsum, 避免添加后, 减去k, 已经出现在里面
2.计算ans
3. 再添加cumsum 进现在的d



class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        self.ans = 0
        self.dfs(root, d, targetSum, 0)
        
        return self.ans
        
        
        
    def dfs(self, node, d, targetSum, pathSum):
        if not node:
            return
        
        pathSum += node.val
        if pathSum - targetSum in d:
            self.ans += d[pathSum - targetSum] if d[pathSum - targetSum] > 0 else 0
        d[pathSum] += 1
        self.dfs(node.left, d, targetSum, pathSum)
        self.dfs(node.right, d, targetSum, pathSum)
        d[pathSum] -= 1 #回朔