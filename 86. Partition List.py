开两个新的node, 一个拼接小于的, 另外一个拼接大于等于
最后让lower_tail.next = higher.next 就拼接完成

但是要注意, higher_tail.next 要设置成None, 否则可能会出现环



class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lower = lower_tail = ListNode(0)
        higher = higher_tail = ListNode(0)
        
        while head:
            if head.val < x:
                lower_tail.next = head
                lower_tail = lower_tail.next
            else:
                higher_tail.next = head
                higher_tail = higher_tail.next
            head = head.next
        higher_tail.next = None
        lower_tail.next = higher.next
        return lower.next