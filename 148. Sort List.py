class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(4)
b = ListNode(3)
c = ListNode(2)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        left = head
        mid = self.find_middle(head)
        right = mid.next
        mid.next = None  #重点, 不要忘记断开链表 !!!
        return self.mergeNode(self.sortList(left), self.sortList(right))
        
        
    def find_middle(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
                              
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def mergeNode(self, node1, node2):
        dummy = head = ListNode(-1)
        
        while node1 and node2:
            if node1.val < node2.val:
                head.next = node1
                node1 = node1.next
            else:
                head.next = node2
                node2 = node2.next
            head = head.next
            
        if node1:
            head.next = node1
        if node2:
            head.next = node2
        
        return dummy.next