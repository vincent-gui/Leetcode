# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        cnt = 0
        node = head
        while node:
            node = node.next 
            cnt += 1

        k %= cnt
        if k == 0: #这里K == 0 非常重要
            return head
        
		
        fast = slow = head    
        #让fast 先走k 步, 这样最后fast到达tail的以后, slow 和fast 就相差k 个node
		while k > 0:
            fast = fast.next
            k -= 1
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None #这一步很重要, 否则会出现环
        fast.next = head
        
        return new_head
            
            
        