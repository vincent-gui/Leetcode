class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class AllOne:

    def __init__(self):
        self.d = {}
        self.head = ListNode(None, -1)
        self.tail = ListNode(None, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def inc(self, key: str) -> None:
        if key not in self.d:
            node = ListNode(key, 0)
            self.d[key] = node
            node.val += 1
            
            last_node = self.tail.prev
            last_node.next = node
            node.next = self.tail
            self.tail.prev = node
            node.prev = last_node
        else:
            node = self.d[key]
            node.val += 1
            while node != self.head.next and node.prev.val < node.val:
                prev_node = node.prev
                prev_prev = prev_node.prev
                nxt = node.next
                
                node.prev = prev_node.prev
                prev_node.next = node.next
                node.next = prev_node
                prev_node.prev = node
                if prev_prev:
                    prev_prev.next = node
                if nxt:
                    nxt.prev = prev_node


    def dec(self, key: str) -> None:
        node = self.d[key]
        node.val -= 1
        if node.val == 0:
            del self.d[key]
            prev_node, next_node = node.prev, node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return
        while node != self.tail.prev and node.next.val > node.val:
            next_node = node.next
            nxt_nxt = next_node.next
            prev = node.prev
            
            node.next = next_node.next
            next_node.prev = node.prev
            node.prev = next_node
            next_node.next = node
            if nxt_nxt: nxt_nxt.prev = node
            if prev: prev.next = next_node
            
 

    def getMaxKey(self) -> str:
        return self.head.next.key if self.head.next.key else ''
        

    def getMinKey(self) -> str:
        return self.tail.prev.key if self.tail.prev.key else ''
        
