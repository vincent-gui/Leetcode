第二种解法

先循环到left node 之前的node , 然后做right - left + 1 次, 这样curr 指向了5, 返回4 和1 拼接

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2) 
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next #move prev to 1 node before left
            
        node = prev.next
        reverse = None
        for i in range(right - left + 1):
            nxt = node.next
            node.next = reverse
            reverse = node 
            node = nxt
        
        #now, reverse node epoint to 4, node point to 5
        prev.next.next = node #注意这两个顺序不可以颠倒, 因为此时1还指向2, 所以要让2 先指向5, 才可以更新1.next = 4
        prev.next = reverse
        
        return dummy.next
            
        
Solution().reverseBetween(a, 2,4)


解法1 扫两边, 第一遍找到left node之前的一个node, 第二遍扫到right node , 反转中间, 连接两侧
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left_prev = self.findNth(dummy, left - 1)
        left_node = left_prev.next
        right = self.findNth(dummy, right)
        right_after = right.next
        right.next = None
        left_prev.next = self.reverse(left_node)
        left_node.next = right_after
        
        return dummy.next
        
    def reverse(self, node):
        dummy = None
        while node:
            nxt = node.next
            node.next = dummy
            dummy = node
            node = nxt
        
        return dummy
    
    def findNth(self, node, k):
        for i in range(k):
            node = node.next
        return node
        