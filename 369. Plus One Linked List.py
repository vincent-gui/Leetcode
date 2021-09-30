第二种解法 DFS, 用carry 作为返回值

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry = self.dfs(head)
        if carry:
            node = ListNode(carry)
            node.next = head
            return node
        return head
        
        
    def dfs(self, node):
        if not node:
            return 1
        carry = self.dfs(node.next)
        carry, node.val = divmod(node.val + carry, 10)
        return carry



第一种解法
思路, 整体倒过来, 加1, 注意最后一个node 就得中断了, 否则返回的是node

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        curr = new_node = self.reverse(head)
        carry = 1
        while curr:
            carry, curr.val = divmod(curr.val + carry, 10)
            if curr.next is None:
                if carry:
                    curr.next = ListNode(carry)
                break
            curr = curr.next
        return self.reverse(new_node) #这里需要传入返回的新的node

  
    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        return prev