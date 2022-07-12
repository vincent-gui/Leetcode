给了一串数组, 问返回一个数组, 每个位置包含当前位置后小于当前位置数字的个数

nums = [5,2,6,1]
返回   [2,1,1,0]



解法1: 

传统segmentTree 解法, 中心思想是扫描一遍当前nums, 找到最大和最小的两个数字, 然后基于这两个分别作为start 和end
例子中就是1和6, 建立一个6位的, 每个node.cnt = 0 的segmentTree
[1,2,3,4,5,6]
[0,0,0,0,0,0]

然后倒序遍历, 对于每一个数字去update leaf node 的cnt , cnt += 1, 然后再query 一下, 这样每次update 完, 
query 用的是query(min, num - 1) 去检索

这种实现方法的缺点tree 太大, 其实还可以用另一种array 类型的segment tree, 实现如下
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/1771441/Python-Segment-Tree-For-Beginners

class SegmentTreeNode:
    def __init__(self, start, end, cnt = 0):
        self.start, self.end = start, end
        self.cnt = cnt

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        mi, mx = min(nums), max(nums)
        root = self.build(mi, mx)
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            self.modify(root, nums[i])
            if nums[i] > mi:
                ans[i] = self.query(root, mi, nums[i] - 1)
        
        return ans
        
        
    def build(self, start, end):
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        
        return root
    
    def modify(self, root, idx):
        if root.start == idx and root.end == idx:
            root.cnt += 1
            return 
        mid = (root.start + root.end) // 2
        if idx <= mid:
            self.modify(root.left, idx)
        else:
            self.modify(root.right, idx)
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start <= root.start and root.end <= end:
            return root.cnt
        if root.end < start or root.start > end:
            return 0
        return self.query(root.left, start, end) + self.query(root.right, start, end)
	
解法2:	
		
上面的解法需要根据数组的最大最小值中间的每一位去构建一个segment tree, 但是segment tree 本身更多应该是基于数组的index 构建
就有了下面的一个improve

主要的改进是用一个numsWithsort 保存 有序, 无重复的数组, 这个时候每个数字在这个数组中的index 就是数字本身的代表

例如
Input: nums = [5,2,6,1, 2]
Output: [2,1,1,0]

排序数组 [1, 2, 5, 6] 
idx 	 [0, 1, 2, 3]

构建一个dict{1:0, 2:1, 5:2, 6:3}

然后倒序遍历nums, 每次用num 对应的idx 去update cnt 然后查询query(0, d[num] - 1) 这个范围, 看看有多少

class SegmentTreeNode:
    def __init__(self, start, end, cnt = 0):
        self.start, self.end = start, end
        self.cnt = cnt

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        numsWithsort = sorted(set(nums))
        d = { v: i for i, v in enumerate(numsWithsort)}
        root = self.build(0, len(numsWithsort) - 1)
        ans = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            self.modify(root, d[nums[i]])
            if nums[i] > numsWithsort[0]:
                ans[i] = self.query(root, 0, d[nums[i]] - 1)
        
        return ans
        
        
    def build(self, start, end):
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        
        return root
    
    def modify(self, root, idx):
        if root.start == idx and root.end == idx:
            root.cnt += 1
            return 
        mid = (root.start + root.end) // 2
        if idx <= mid:
            self.modify(root.left, idx)
        else:
            self.modify(root.right, idx)
        root.cnt = root.left.cnt + root.right.cnt
        
    def query(self, root, start, end):
        if start <= root.start and root.end <= end:
            return root.cnt
        if root.end < start or root.start > end:
            return 0
        return self.query(root.left, start, end) + self.query(root.right, start, end)