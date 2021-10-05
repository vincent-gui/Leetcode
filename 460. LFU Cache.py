解法: 用一个ordereddict 去track 同一个frequency 的node 的先后顺序
popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

move_to_end(key, last=True)
Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

class Node(object):
    def __init__(self, key, val, count=1):
        self.key = key
        self.val = val
        self.count = count

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #int: count to track capacity
        #dict: to track all nodes
        #orderdict: to track sequence for each frequency
        #int: to track min frequency
        
        self.capacity = capacity
        self.nodes = {}
        self.frqucy_to_nodes = defaultdict(OrderedDict)
        self.min = None
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #check key present
        if key not in self.nodes:
            return -1
            
        curr_node = self.nodes[key]
        del self.frqucy_to_nodes[curr_node.count][key]
        
        #clean frqucy_to_nodes if that frequency without any node
        if not self.frqucy_to_nodes[curr_node.count]: #注意!!!这里需要检测这个frequency 是否还有任何node
            del self.frqucy_to_nodes[curr_node.count]
            
        curr_node.count += 1
        self.frqucy_to_nodes[curr_node.count][key] = curr_node
        
        if not self.frqucy_to_nodes[self.min]: #注意!!! 这个需要更新最小的frequency
            self.min += 1
        
        return curr_node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.capacity:
            return 
        #check if key in self.nodes
        if key in self.nodes:
        #yes do update
            self.nodes[key].val = value
            self.get(key)
            return 
        
        if self.capacity == len(self.nodes):
            #pop the leaset fre node
            k, v = self.frqucy_to_nodes[self.min].popitem(last = False)
            del self.nodes[k]
        
        self.frqucy_to_nodes[1][key] = self.nodes[key] = Node(key, value, 1)
        self.min = 1
        return 

        
            
        
        
        #insert node
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)