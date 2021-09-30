# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_start = even = ListNode(-1)
        odd_start = odd = ListNode(-1)
        
        if not head:
            return None
        

        while head and head.next:
            even.next = head
            odd.next = head.next
            head = head.next.next
            even = even.next
            odd = odd.next
        
        odd.next = None #断开最后一个odd的链接， 否则会出现环
        if head and not head.next: #判定最后是不是还剩一个node
            even.next = head
            even = even.next
        
        even.next = odd_start.next
        
        return even_start.next
            
        
            

参考答案, 第一个node 为odd， 第二为even 只判定even 存在就可以
class ListNode:
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

class Solution:
    def oddEvenList(self, head) :
        if head is None:
            return head
        odd = head
        evenHead = head.next
        even = evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
        
Solution().oddEvenList(a)
