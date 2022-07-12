题目: 构建segment Tree, 
给了一个初始数组[1, 3, 5], 基于这个数组构建一个segment Tree

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8



class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start, self.end, self.val = start, end, val
        self.left, self.right = None, None
        

class NumArray:
    
    def build(self, start, end, nums):
        node = SegmentTreeNode(start, end, nums[start]) #!!!!注意构建segment Tree 的时候用的是数组的长度作为start, end , #而不是数组的最大最小值, 这点非常重要( 否则315 题就会超时)
        if start == end:
            return node
        mid = (start + end) // 2
        node.left = self.build(start, mid, nums)
        node.right = self.build(mid + 1, end, nums)
        node.val = node.left.val + node.right.val
        
        return node
    
    def modify(self, node, index, val):
        if node.start == index and node.end == index:
            node.val = val
            return node.val
        mid = (node.start + node.end) // 2
        if index <= mid:
            self.modify(node.left, index, val)
        else:
            self.modify(node.right, index, val)
        node.val = node.left.val + node.right.val
        
    def query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.val
        if start > node.end or end < node.start:
            return 0
        return self.query(node.left, start, end) + self.query(node.right, start, end)

    def __init__(self, nums: List[int]):
        self.root = self.build(0, len(nums) - 1, nums)

    def update(self, index: int, val: int) -> None:
        self.modify(self.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.query(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)