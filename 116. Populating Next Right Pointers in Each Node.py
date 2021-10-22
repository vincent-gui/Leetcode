总结： 用一个next_level 去track 下一层， 然后， 循环当前层， 每一次都先保证root.left 指向 root.right， 接着让node.right 指向node.next.left， 再让node = node.next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        curr = root
        next_level = root.left
        
        while next_level:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = next_level
                next_level = curr.left
        
        return root