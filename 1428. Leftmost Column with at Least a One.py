题目, 一个matrix, 每一行都是排好序的, 问包含1 且idx 最左的那个index 是什么

一开始想的binary search, 每行循环, 然后每行binary search, time 就是N * lnM

后来找到M + n

从右上顶点开始, 如果遇到是0 ,则row += 1, 如果是1, 则col -= 1, 并且更新答案

最后返回


class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
                    
        n, m = binaryMatrix.dimensions()
        row, col = 0, m - 1
        ans = -1
        
        while row < n and col >= 0:
            if binaryMatrix.get(row, col) == 0:
                row += 1
            else:
                ans = col
                col -= 1
        
        return ans