思路: A, B 两个数组, 从A 任意劈一刀, 总长的一半减去A 这一刀, 就应该是B 的左半部分的长度,

如果是中位数, 那么意味着
l1   r1
l2   r2
的关系是 

l1 必须小于r1 同时必须小于 r2
l2 必须小于r1 同时必须小于 r2

如果l1 大于 r2, 意味着第一个数组批的那一刀偏右了, 所以需要让end = 劈点 - 1
如果l2 大于 r1, 意味着第一个数组批的那一刀偏左了, 所以需要让start = 劈点 + 1

如果不满足上面两个, 就以为左半部分全部小于右半部分, 右因为左半部分的总长等于两数组总长的一半, 所以这个时候就是结果




class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            return self.help(nums1, nums2)
        else:
            return self.help(nums2, nums1)
        
        
    def help(self, A, B):
        length = len(A) + len(B)
        start, end = 0, len(A)
        
        while start <= end:
            cutA = (start + end) / 2
            cutB = length / 2 - cutA
            l1 = A[cutA - 1] if cutA != 0 else -sys.maxint
            r1 = A[cutA] if cutA != len(A) else sys.maxint
            l2 = B[cutB - 1] if cutB != 0 else -sys.maxint
            r2 = B[cutB] if cutB != len(B) else sys.maxint
            
            if l1 > r2: #这里为什么不可以是>=  ?????
                end = cutA - 1
            elif l2 > r1: #这里为什么不可以是>=  ??????
                start = cutA + 1
            else:
                if length % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) * 1.0 / 2
                else:
                    return min(r1, r2)
    