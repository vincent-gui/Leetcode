题目: 给一个数组, 排序的, 里面没有重复, 然后给一个k, 就问, 第k 个missing 的number 是什么


解法, 首先需要明白arr[idx] - idx - 1 就表示到当前idx 有多少个数missing了

idx = [0,1,2,3,4]
arr = [2,3,4,7,11]
    = [1,2,3,4,5]
miss= [1,1,1,3,6] 这个数组是一个prefix_missing 的数组, 

这个题和1060 很像, 但是1060 比这个题简单, 因为那个题不需要考虑arr 之前的数, 类似于arr = [6,7,8] k = 1,2,3,4 


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] - mid - 1 == k:#num - idx - 1 is how many missing, 用这个多少个missing k 比较
                end = mid 
            elif arr[mid] - mid - 1 < k:
                start = mid
            else:
                end = mid
        if arr[end] - end - 1 < k: #先比较大的, 如果不满足, 在比较start
            return arr[end] + (k - arr[end] + end + 1)
        if arr[start] - start - 1 < k: #如果这里还是不满足, 那么只有一种情况  arr = [6,7,8] k = 1,2,3,4
            return arr[start] + (k - arr[start] + start + 1)
        return k #所以这里只需要return k