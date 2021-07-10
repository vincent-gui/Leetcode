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


这个顺序保证了最后不会多出一个空node

carry一个变量就够了, 每次都是carry += v1 or v2


class ListNode(object):
	def __init__(self, val=0, next=None):
			self.val = val
			self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(None)  #创建一个dummy node, 最后返回的时候用
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            carry, num = divmod(carry, 10)
            node.next = ListNode(None) 
            node = node.next #创建第一个node, 并且把curr 指针指向这个新创建的node, head 还是保留最开始的node 上
            node.val = num #给当前node 赋值

        return head.next
        

            
                
                
                
            