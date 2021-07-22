
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