这个题思路不难,

第一抓出k个node, 丢进去反转, 同时保留最开始的node(反转后的最后一个) 让这个node 指向下一个反转的结果
反转内部返回新的head


递归的步奏,
1. 定义递归出口
2. 写出连接方程
3. 写出返回值

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        node = head
        
        cnt = 0
        while node and cnt < k:
            node = node.next
            cnt += 1
        #node 是尾巴的下一个
        
        #退出条件
        if cnt < k:
            return head
        
        new_head = self.reverse(head, k)
        head.next = self.reverseKGroup(node, k)
        return new_head
        
        
        
    def reverse(self, node, k):
        
        dummy = ListNode(None)
        dummy.next = node
        
        while k > 0:
            next_node = node.next
            node.next = dummy
            dummy = node
            node = next_node
            k -= 1
        return dummy
Solution().reverseKGroup(a, 2)