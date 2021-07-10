总结, 这样需要返回新的一条linkedlist 或者tree 的时候, 

正序
1. 创建header 和 curr node
2. 先计算好值(node.val)
3. 基于第二步的val, 创建新的node
4. 让curr 移动到新的node上
返回header.next

倒序
1. node = None  #创建最后一个 node
2. head = listNode(val) #循环创建起始node
3. head.next = node #起始node 指向最后一个node
4. node = head #最后一个node = 起始node
最后返回head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        node = None
        
        
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, num = divmod(carry, 10)
            header = ListNode(num)
            header.next = node
            node = header
        
        return header
