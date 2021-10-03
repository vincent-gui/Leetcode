
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        
a = Node(7)
b = Node(8)
c = Node(9)
d = Node(10)
e = Node(11)
f = Node(12)
a.next = b
b.next = c
c.next = d
e.next = f
f.prev = e
d.prev = c
c.prev = b
b.prev = a
b.child = e


方法1, stack, 先将node.next 放入stack, 再将node.child 放入stack

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return 
        dummy = prev = Node(-1)
        dummy.next = head
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            prev.next = curr
            curr.prev = prev
            
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                curr.child = None #注意这里千万要把child 放置为None
            
            prev = curr
        dummy.next.prev = None
        
        return dummy.next
        
Solution().flatten(a)


#方法2 对于flat 做递归, 但是内部child 展平的过程做loop, 最后一个结点的时候, 让预先存好的nxt_node和展平的最后一个结点连接, 并且返回最新的节点
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return 
        
        node = head
        while node:
            if node.child:
                flatten_node = self.flatten(node.child)
                node.child = None
                nxt_node = self.move_to_flatten_end(node, flatten_node)
                node = nxt_node
            else:
                node = node.next
        
        return head
                
                
    def move_to_flatten_end(self, node, flatten_node):
        nxt_node = node.next
        node.next = flatten_node
        flatten_node.prev = node
        while node.next:
            node = node.next
        if nxt_node:
            node.next = nxt_node
            nxt_node.prev = node
        return nxt_node
        
 方法3: 这个解法精妙的在于用一个新的dfs, 把child 和next 放进了同一个level 的recrusive 里,牛逼!!!!, 传入了上一个node 和下一个node 
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        dummy = Node(-1)
        self.dfs_flatten(dummy, head)
        dummy.next.prev = None
        
        return dummy.next
        
        
        
    def dfs_flatten(self, prev, curr):
        if not curr:
            return prev
        
        prev.next = curr
        curr.prev = prev
        
        temp_next = curr.next
        tail = self.dfs_flatten(curr, curr.child)
        curr.child = None
        return self.dfs_flatten(tail, temp_next)