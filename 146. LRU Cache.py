class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        #get Node
        #move to head
        if key not in self.d:
            return -1
        else:
            node = self.d[key]
            self.remove_node(node)
            self.move_to_head(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        #insert or replace
        #move to head
        #delete extra code
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove_node(node)
        else:
            node = ListNode(key, value)
            if len(self.d) == self.capacity:
                last_node = self.tail.prev
                del self.d[last_node.key]
                self.remove_node(last_node)
            self.d[key] = node  
        self.move_to_head(node)
        
        
        
    def move_to_head(self, node):
        first = self.head.next
        node.next = first
        first.prev = node
        self.head.next = node
        node.prev = self.head
        
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
l = LRUCache(2)
l.put(1,0)
l.put(2,2)
l.get(1)
l.put(3,3)
l.get(2)
l.put(4,4)
l.get(1)
l.get(3)
l.get(4)