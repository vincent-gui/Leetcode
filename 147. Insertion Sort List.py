总结: 创建一个dummy node, 每次从head 开始搜索, 找到一个能够插入的节点, 和dummy 连接, 连接完再重新从dummy 开始扫描


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        
        curr = head
        
        while curr:
            prev = dummy
            
            #从头开始查找比curr 大的节点, 插入
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            nxt = curr.next
            curr.next = prev.next
            prev.next = curr
            
            curr = nxt
        
        return dummy.next
		
		
		
插入排序
def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 