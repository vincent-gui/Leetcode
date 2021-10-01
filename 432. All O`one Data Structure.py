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
        
根骨清奇的解法

答题思路是: 有起始和end, 如果是新的, 就放在beigin node 之后, 如果是存在的, 那么在current 节点后添加一个新的结点, 并且val 是current node + 1, 然后从上一个node 的set 里删除掉自己, 这里还考虑到如果出现了两个相同频率的, 放在同一个节点(画龙点睛之笔!!!!!) 牛逼

class Block(object):
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block


class AllOne(object):
    def __init__(self):
        self.begin = Block()  # sentinel
        self.end = Block()  # sentinel
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}  # key to block

    def inc(self, key):
        if not key in self.mapping:  # find current block and remove key
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.after.val:  # insert new block
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        new_block.keys.add(key)  # update new_block
        self.mapping[key] = new_block  # ... and mapping of key to new_block

        if not current_block.keys and current_block.val != 0:  # delete current block if not seninel
            current_block.remove()

    def dec(self, key):
        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]  # could use self.mapping.pop(key)
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.before.val:  # insert new block
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:  # delete current block
            current_block.remove()

    def getMaxKey(self):
        if self.end.before.val == 0:
            return ""
        key = self.end.before.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.end.before.keys.add(key)
        return key

    def getMinKey(self):
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key