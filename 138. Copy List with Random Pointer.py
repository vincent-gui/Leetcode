总结, 用mapping 保存映射关系,两次循环
第一次创建duplicate node, 并且连接next
第二次用映射, 连接random 关系

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        mapping = {}
        prev = None
        node = head
        
        while head:
            mapping[head] = Node(head.val)
            if prev:
                prev.next = mapping[head]
            prev = mapping[head]
            head = head.next
        
        head = node
        
        while head:
            copyNode = mapping[head]
            randomNode = head.random
            copyNode.random = mapping[randomNode] if randomNode else None #注意这一行, 要判断是否指向了None
             
            head = head.next
        
        return mapping[node]
		
		

第二种解法, 不需要额外空间
思路
1. 每个点建立新的node, 新node 指向下一个node, 让原来的node 指向新node
2. 复制random 指向
3. 拆分奇偶
		p = head 
        dummy = ListNode(-1)
        copy_p = dummy
        while p: 
            copy_p.next = p.next 
            copy_p = copy_p.next 
            p.next = p.next.next
            p = p.next 
        return dummy.next 
            

class ListNode:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
a = ListNode(7,13,None)
b = ListNode(13, 11, a) 
c = ListNode(11, 10)
d = ListNode(10, 1, c)
e = ListNode(1, None, a)
c.random = e

a.next = b
b.next = c
c.next = d
d.next = e


class Solution(object):
    def copyRandomList(self, head):
        if not head: 
            return head
        # 复制影子节点
        p = head 
        while p: 
            add_node = ListNode(p.val)
            add_node.next = p.next 
            p.next = add_node
            p = p.next.next 
        # 复制随机指针
        p = head 
        while p: 
            if p.random: 
                p.next.random = p.random.next 
            p = p.next.next
        #　奇偶链表拆分
        p = head 
        dummy = ListNode(-1)
        copy_p = dummy
        while p: 
            copy_p.next = p.next 
            copy_p = copy_p.next 
            p.next = p.next.next
            p = p.next 
        return dummy.next 
            
        
Solution().copyRandomList(a)