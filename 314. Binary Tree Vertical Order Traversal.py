解法: 因为要求答案输出是从上到下, 从左到右, 最好用BFS

这个解法的时间复杂度是Nlgn, 因为如果只有左子树, 那么排序的时间复杂度就是nlgn

follow up, 有没有办法优化时间复杂度

就用两个变量max_left, max_right初始为0, 每一个向左或者向右移动, 就去更新max_left, max_right, 这样最后d 里的结果一定是连续的, 并且边界就是max_left 到max_right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        d = {}
        while queue:
            node, x = queue.popleft()
            if x not in d:
                d[x] = [node.val]
            else:
                d[x].append(node.val)
            if node.left:
                queue.append((node.left, x - 1))
            if node.right:
                queue.append((node.right, x + 1))
        
        return [d[key] for key in sorted(d.keys())]