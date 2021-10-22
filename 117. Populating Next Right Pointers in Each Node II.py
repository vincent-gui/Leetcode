总结, 每一层create 一个dummynode, dummy.next 就是下一层的最左侧的node

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        node = root
        
        while node:
            curr = dummy = Node(-1)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = node.left
                if node.right:
                    curr.next = node.right
                    curr = node.right
                node = node.next
            node = dummy.next
        
        return root