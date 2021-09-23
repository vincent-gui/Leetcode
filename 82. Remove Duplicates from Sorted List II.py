two point , slow 指向最后一个不重复的node, fast 做循环, 跳过重复node, 判断slow.next == fast, 等于同时前进, 不等于直接跳过重复


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        fast = head
        dummy = slow = ListNode(None)
        slow.next = fast
        
        
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            
            if slow.next == fast:
                slow = slow.next
                fast = fast.next
            else:
                slow.next = fast.next
                fast = fast.next
        
        return dummy.next