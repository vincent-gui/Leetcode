题目: 两个稀疏数组, 求 相同index 的数乘机 和
比如: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
				1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
				
思路: 很多人可能会想到用dict, 因为这样判断快, 但是如果数组非常的, build dict 就会很费时间, 因为需要resize, 这个时候就不如用数组更好



follow up 如果只有一个是系数矩阵, 怎么办????
	答案 遍历短的, 给长的做Binary search, 这样time 是 Klg(n)
	https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/1823242/Clean-solutions-for-meta-interview-with-potential-follow-ups
	
	
相似题:  311. Sparse Matrix Multiplication
class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.list = []
        for i, num in enumerate(nums):
            if num != 0:
                self.list.append((i, num))
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        l = r = 0
        ans = 0
        
        while l < len(self.list) and r < len(vec.list):
            if self.list[l][0] == vec.list[r][0]:
                ans += self.list[l][1] * vec.list[r][1]
                l += 1
                r += 1
            elif self.list[l][0] < vec.list[r][0]:
                l += 1
            else:
                r += 1
        
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)