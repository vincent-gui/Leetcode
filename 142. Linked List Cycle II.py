思路
快慢指针, 快指针一次两步, 慢指针一次一步
相遇后将慢指针指向head, 快指针慢指针都一次一步, 相遇就是起始点

注意判断是否有环

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None: #这一行很重要
            return 
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

                
        if fast == slow: #如果不相等, 那就没有环, 直接返回None
            slow = head
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
        
        return None