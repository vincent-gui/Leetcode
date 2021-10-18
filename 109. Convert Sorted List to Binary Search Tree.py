class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
a = ListNode(-10)
b = ListNode(-3)
c = ListNode(-1)
d = ListNode(0)
e = ListNode(5)
f = ListNode(9)
g  = ListNode(19)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



解法1: 遍历一边linkedlist, 把每个点存进list 里, 然后常规递归找中点就可以
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        return self.buildBST(nums)
        
        
    def buildBST(self, nums):
        if nums:
            mid = len(nums) / 2
            node = TreeNode(nums[mid])
            node.left = self.buildBST(nums[:mid])
            node.right = self.buildBST(nums[mid + 1:])
            return node
			
			
解法2. 这个解法很有意思
首先找到整个LinkedList 的长度, 然后做二分, 这里用到了inorder traversal 的思想, 一个指针指向linkedlist 的头, 一个一个逐一扫描, 
convert 函数内部, 首先就是左循环, start + end // 2, 然后, 一直左侧, 直到找到最左侧的点, 这个点起始也是linkedlist 的head, 利用inorder 左中右, 一步一步从bottom up 的方式建立整个list

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size = self.find_size(head)
        self.curr = head
        
        return self.convert(1, size)
        
        
    def convert(self, start, end):
        if start > end:
            return 
        
        mid = (start + end) // 2
        left_node = self.convert(start, mid - 1)
        curr_node = TreeNode(self.curr.val)
        curr_node.left = left_node
		#前边这三步就是递归, 然后将左孩子分给node.left
		
        self.curr = self.curr.next #linkedlist 向下继续走
		
        curr_node.right = self.convert(mid + 1, end) 
        return curr_node
        
        
    def find_size(self, node):
        size = 0
        while node:
            size, node = size + 1, node.next
        
        return size