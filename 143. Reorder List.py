12/21/2021
反转链表可以用
prev, curr = None, slow
while curr:
	curr.next, prev, curr = prev, curr, curr.next 
	
合并链表可以用
while first and second:
	first.next, first = second, first.next
	second.next, second = first, second.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#第二种解法 前半部分一样, 找中点的前一个, 后半部分直接丢进stack里
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right_node = slow.next
        slow.next = None
        while right_node:
            stack.append(right_node)
            right_node = right_node.next
            
        node = head
        
        while stack:
            insert_node = stack.pop()
            insert_node.next = node.next
            node.next = insert_node
            node = node.next.next
        
        return head
        
        

#解法1 找 linkedin List 中点前一个点 + 反转后半部分 + 合并node
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right_node = slow.next
        slow.next = None
        node2 = self.reverse(right_node)
        
        node1 = head
        while node1 and node2:
            nxt = node1.next
            node1.next = node2
            node1 = nxt
            nxt = node2.next
            node2.next = node1
            node2 = nxt
            
        return head
    
    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        return prev
            




    