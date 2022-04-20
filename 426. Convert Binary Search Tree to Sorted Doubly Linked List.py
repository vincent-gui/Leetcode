题目: 将一个bst 变成双向链表, left 指向钱一个node, right 指向后一个node

解法: 和一般的tree 的题目不太一样, 因为每一层dfs 其实不需要return 任何东西, 用两个glable 的变量, 一个指向开始, 一个指向结束

inorder 就可以, 如果有last , 那么last 和curr update, 没有则赋值first 为初始node

创建dummy node 和这个原理一致



class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        self.last, self.first = None, None
        self.dfs(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first
        
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        
        if self.last:
            self.last.right = node
            node.left = self.last
        else:
            self.first = node
        self.last = node
        
        self.dfs(node.right)