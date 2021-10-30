解法1 以第一个值为root, 从idx 1 ~ len(preorder) 遍历, 找到第一个大于root 的值, 那么就意味着, 这个值左边都属于root 的左子树, 右边属于root 的右子树, 然后以这个值的index 为界限. 左边右边同时递归查找

时间复杂度O(nlgn) 每次检索需要scan O(n), 深度lgN
举例
ZXxxYyy
如果Y 是第一个大于Z 的值, 这个时候左右同时递归, Xxx, 再次递归, 又会重新扫描一遍Xxx, 同理Yyy


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder or len(preorder) == 1:
            return True
        curr = preorder[0]
        i = 1
        while i < len(preorder):
            if preorder[i] > curr:
                break
            i += 1

        for j in range(i, len(preorder)):
            if preorder[j] < curr:
                return False
        left = self.verifyPreorder(preorder[1:i])
        right = self.verifyPreorder(preorder[i:])
        if left and right:
            return True
        return False
		
解法2. 单调栈  具体解法就是往栈里放, 如果current > stack[-1] 就pop, 直到 把栈pop 空, 再把curr 加进去, 并且要检查, 最后一个pop 出来的 是否大于 current value


视频讲解 https://www.youtube.com/watch?v=0kkVobZ6Ebc



class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        last, stack = None, []
        
        for node in preorder:
            #check if need pop out
            while stack and node > stack[-1]:
                last = stack.pop()
            #check if last greater than current value
            if last and last > node:
                return False
            #add item into stack
            stack.append(node)
        return True