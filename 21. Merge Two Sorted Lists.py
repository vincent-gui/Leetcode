#解法2, 递归
递归三要素
1. 结束条件
2.传导方程
3.返回关系

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            



解法1: 归并
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            else:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
        
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        
        return head.next