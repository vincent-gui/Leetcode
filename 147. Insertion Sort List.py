总结: 创建一个dummy node, 每次从head 开始搜索, 找到一个能够插入的节点, 和dummy 连接, 连接完再重新从dummy 开始扫描


12/15/2021
   #开一个新的头dummy， 往这个新的头里insert， 一个变量一直track 当前的curr， 另外一个每次从dummy 开始， 找到比curr。val 大的那个之前， 插入进去， 然后让curr 向前移动一位， prev 重制到dummy， 继续从头开始

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