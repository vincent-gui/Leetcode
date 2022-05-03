题目就是右上-左下遍历matrix

思路:
	用一个k判定现在是向右上还是左下
	循环 m * n 次
	
	每次先将现在位置的数放进结果, 
	!!!巧妙的是di, dj 的使用, 当未越界时, 反向赋值给i,j, 如果越界, 舍弃di, dj, 后对i, j 操作

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        #k = 1 up-right
        #k = -1 down-left
        
        i, j, k = 0, 0, 1
        n, m = len(mat), len(mat[0])
        ans = []
        
        for _ in range(n * m): #
            ans.append(mat[i][j])
            
            #check up-right
            if k > 0:
                di, dj = i - 1, j + 1
            else: # is down-left
                di, dj = i + 1, j - 1
            
            #check reach out to edge
            if 0 <= di < n and 0 <= dj < m:
                i, j = di, dj
            else: # need to switch to next line
                if k > 0:
                    if j + 1 < m:  #未到右边界, 那么右移, !!!需要验证的是右边界, 而不是 i 是否小于0, 否则在右上角会越界
                        j += 1
                    else:
                        i += 1 #否则下移
                else:
                    if i + 1 < n: #未到下边界, 下移
                        i += 1
                    else:  #否则 右移
                        j += 1
                k *= -1
        return ans
                