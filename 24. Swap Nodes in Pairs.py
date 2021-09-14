解法2
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 保存第二个node, 将第三个节点做递归, 返回的结果被第一个节点指向 , 第二个节点指向第一个节点
        if not head or not head.next:
            return head
        #head 是第一个节点, head.next 是第二个节点
        curr = head.next
        head.next = self.swapPairs(head.next.next)
        curr.next = head
        return curr


解法1:
思路: 和最初自己的思路是一样的, 唯一的区别是, 只需要控制主一个curr 点的前进就可以

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(None)
        curr.next = head
        
        while curr.next and curr.next.next: #这里可以控制, 单个点不需要swap
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next #精华, 这个点就是将curr -> 1 -> 2 推进到 1->2(curr)->3->4
        return dummy.next






class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d