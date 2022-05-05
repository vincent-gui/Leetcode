题目: 给一个排序数组, 返回k个离x 最近的数, 按照从小到大排序

解法: 因为要k个数字, 其实left pointer 其实最多就能到 len(arr) - k 

当left 固定后, window 的左和右的和的平均值相比较于x, 如果x > 这个平均值,那么意味着 需要把left 向右移动1 位, 增大这个平均值


time: Log(n-k) + k
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k # 表示left 的坐标最多取到len(arr) - k 
		
        
        while left < right:
            mid = (left + right) // 2  #mid 就是在寻找left 到底可以在哪
            if x > (arr[mid] + arr[mid + k])/2:  #当left 固定后, window 的左和右的和的平均值相比较于x, 如果x > 这个平均值,那么意味着 需要把left 向右移动1 位, 增大这个平均值
			#这里为什么没有等号的原因是要使得所有的结果向左倾斜, 也就是偏小
			#[1,2,3,4,5], target 是3, 找4个数, 结果希望是[1,2,3,4], 而不是[2,3,4,5]
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]



time: Log(n) + klg(K)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        start, end = 0, len(arr) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid
        
        left, right = start, end
            
        ans = []
        
        while len(ans) < k:
            left_diff = abs(arr[left] - x) if left >= 0 else None
            right_diff = abs(arr[right] - x) if right < len(arr) else None
            
            if left_diff is not None and right_diff is not None:
                if left_diff <= right_diff:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            elif left_diff is not None:
                ans.append(arr[left])
                left -= 1
            elif right_diff is not None:
                ans.append(arr[right])
                right += 1
        
        return sorted(ans)
                
                