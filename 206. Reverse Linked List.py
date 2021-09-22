解法1: 定义两个额外的node, 一个是curr = None , 另一个是front, front = head.next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = None
        while head:
            front = head.next
            head.next = curr
            curr = head
            head = front
        
        return curr
#另一种清晰写法	
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        next_node = None
        
        while curr_node:
            next_node = curr_node.next # save next 
            curr_node.next = prev_node # reverse
            prev_node = curr_node #
            curr_node = next_node # advance prev & curr
            
        return prev_node
		
第二种解法, 都需要背会		
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: #这里的目的 其实是为了保证head 会在最后一个node 停住(也是为了head.next.next = head 做准备)
            return head
        tail = self.reverseList(head.next) #这一行的作用就是寻找最后那个点, 并且停在最后, 用以返回
        head.next.next = head #可以使得head的下一个指向head 自己
        head.next = None
        return tail