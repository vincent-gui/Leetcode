思路: 用heap 去做比较, 因为不能直接比较node, 所以要存储node.val 和node

下次可以实现一下merge sort

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = head = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]: #这里需要判断是否为None
                heapq.heappush(heap, (lists[i].val, lists[i]))
        
        while heap:
            val, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            node = node.next
            if node:#这里需要判断是否为None
                heapq.heappush(heap, (node.val, node))
        
        return dummy.next