快慢指针， 慢指针指向head， 快指针指向第二个node， 如果想等， slow.next = fast.next, 否则 slow = slow.next, fast = fast.next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = head
        fast = head.next
        
        while fast and slow:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        
        return head