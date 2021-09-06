总结, 写法是让fast 先走n 步, 然后fast slow 一起走
最后return dummy.next (不可以return head)



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
		fast = head
        slow = dummy #注意前4行, 必须这么写, 得多做几个题,看看是不是都可以这么写
        for i in range(n):
            fast = fast.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next, #为什么一定要return dummy.next, 而不是直接固定head, 最后return head, 是因为, 如果只有一个listnode, 那么head 其实不变, 但是因为dummy.next 已经指向了None, 所以, return head 是错误的
		
