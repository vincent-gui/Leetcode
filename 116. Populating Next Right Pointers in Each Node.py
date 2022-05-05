总结： 用一个next_level 去track 下一层， 然后， 循环当前层， 每一次都先保证root.left 指向 root.right， 接着让node.right 指向node.next.left， 再让node = node.next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        curr = root
        next_level = root.left
        
        while next_level: #判断下一层是否存在, 如果存在, 就连接下一层的点
            curr.left.next = curr.right #这一步就直接把当前node 的做连接到右上了
            if curr.next: #这个条件会一直让这个在当前层传递, 直到最后什么都没有
                curr.right.next = curr.next.left #这一步是为了把不同子树最右的连接到最左
                curr = curr.next
            else:
                curr = next_level
                next_level = curr.left
        
        return root