
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None
            
        root = self.segmentTree(0, len(A) - 1, A)
        
        return root
        
        
    def segmentTree(self, start, end, A):
        if start > end:
            return None
        node = SegmentTreeNode(start, end, A[start])
        
        if start == end:
            return node
        mid = (start + end) / 2
        node.left = self.segmentTree(start, mid, A)
        node.right = self.segmentTree(mid + 1, end, A)
        
        node.max = max(node.max, node.left.max, node.right.max)

            
        return node

    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.max = value
            return root.max
        mid = (root.start + root.end) /2
        if index <= mid:
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        root.max = max(root.left.max, root.right.max)

    def query(self, root, start, end):
        # write your code here

        if root.start == start and root.end == end:
            return root.max
        leftMax = rightMax = -sys.maxint
            
        mid = (root.start + root.end) / 2
        if mid >= end:
            leftMax = self.query(root.left, start, end)
        elif mid < start:
            rightMax = self.query(root.right, start, end)
        else:
            leftMax = self.query(root.left, start, mid)
            rightMax = self.query(root.right, mid + 1, end)
            
        return max(leftMax, rightMax)

test = Solution()
nums=[1,4,2,3]
root = test.build(nums)
#test.modify(root, 4, 10)
test.modify(root, 0, 4)



------------

class segmentTreeNode():
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None


class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if len(A) == 0:
            return [0] * len(queries)
        

        root = self.segmentTree(0, 5)
        
        for num in A:
            self.modify(root, num)
        
        res = []
        for num in queries:
            res.append(self.query(root, 0, num - 1))
            
        return res
        
        
    
    def segmentTree(self, start, end):
        if start > end:
            return 
        node = segmentTreeNode(start, end, 0)
        if start == end:
            return node
        mid = (start + end) / 2
        node.left = self.segmentTree(start, mid)
        node.right = self.segmentTree(mid + 1, end)
        
        return node
        
    def modify(self, root, index):

        if root.start == index and root.end == index:
            root.count += 1
            return
        leftCount = rightCount = 0
        mid = (root.start + root.end) / 2
        if mid >= index:
            self.modify(root.left, index)
        else:
            self.modify(root.right, index)
            
        root.count = root.left.count + root.right.count
    

    
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.count
        
        leftCount = rightCount = 0
        mid = (root.start + root.end) / 2
        if mid >= end:
            leftCount = self.query(root.left, start, end)
        elif mid < start:
            rightCount = self.query(root.right, start, end)
        else:
            leftCount = self.query(root.left, start, mid)
            rightCount = self.query(root.right, mid + 1, end)
            
        return leftCount + rightCount
        
array =[1,2,7,8,5];queries =[1,8,5]
Solution().countOfSmallerNumber(array, queries)



----------------

class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start, self.end, self.sum = start, end, sum
        self.left, self.right = None, None
    

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums or len(nums) == 0:
            return None
        
        self.root = self.segmentTree(0, len(nums) - 1, nums)
        
    def segmentTree(self, start, end, nums):
        node = SegmentTreeNode(start, end, nums[start])
        if start == end:
            return node
        mid = (start + end) / 2
        node.left = self.segmentTree(start, mid, nums)
        node.right = self.segmentTree(mid + 1, end, nums)
        
        node.sum = node.left.sum + node.right.sum
        return node
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        root = self.root
        self.update_helper(root, index, val)
        
        
    def update_helper(self, node, index, val):
        if node.start == index and node.end == index:
            node.sum = val
            return node.sum
        mid = (node.start + node.end) / 2
        if index <= mid:
            self.update_helper(node.left, index, val)
        else:
            self.update_helper(node.right, index, val)
        
        node.sum = node.left.sum + node.right.sum
        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sumRange_helper(self.root, left, right)
        
    def sumRange_helper(self, root, start, end):
        if start <= root.start and root.end <= end:
            
            return root.sum 
            
        if start > root.end or end < root.start:
            
            return 0
            
        return self.sumRange_helper(root.left, start, end) + self.sumRange_helper(root.right, start, end)
        
        

obj = NumArray([1, 3, 5])
obj.sumRange(0, 2)
obj.update(1,2)
obj.sumRange(0, 2)