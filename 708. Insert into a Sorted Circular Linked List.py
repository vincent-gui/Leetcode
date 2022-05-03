题目: 给了一个循环的递增链表, 和一个node , 插入这个node 并且保持链表递增

一开始脑子就晕了, 在考虑怎么判定只有一个node, 因为不知道给的入口的大小, 所以必须需要两个node 才能搞清楚是在链表的什么阶段

又考虑到如果只有一个node, 怎么返回

还有就是考虑循环linkedlist 的循环退出条件
while prev.next != head: 也就意味着只需要循环一次


看了答案以后觉得还是答案厉害

思路:
	一共分成三种情况
	1. 1 < 3 < 5, 3 是需要插入的结点
	2. 5 -> 2 -> 4, 1或者6 是需要插入的结点, 整个时候需要找到 prev.val > curr.val 
	3. 5-> 5-> 5, 2 是需要被插入的结点, 其实任何一个结点插入就可以, 可以合并到第一种情况
	
	
	所以变成两种情况
	1. 1 <= 3 <= 5, 3 是需要插入的结点
	2. 5 -> 2 -> 4, 1或者6 是需要插入的结点, 整个时候需要找到 prev.val > curr.val 
	
解法如下

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)  
        
        if not head:
            node.next = node #注意如果只有一个点, 那么必须指向自己
            return node

        prev, curr = head, head.next
        
        while prev.next != head: #这个退出条件简直就是精华, 为什么??? 相等回到了原点
            # Case1: 1 <- Node(2) <- 3
            if prev.val <= node.val <= curr.val:
                break
            
            # Case2: 3 -> 1, (3 -> Node(4) -> 1 or 3 -> Node(0) -> 1) 大于大的, 或者小于小的
            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
                break
            
            prev, curr = prev.next, curr.next

        # Insert node.
        node.next = curr
        prev.next = node           
        
        return head
