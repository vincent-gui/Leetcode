思路, 
1.精华就是第10行, 用arr1 的起点 和arr2 的终点比较, 并且用arr2 的起点 和arr1 的终点比较, 满足则一定有交集
2.最后判定哪个移动的时候, 用的是谁的终点小, 移动谁 
例如 arr1 = [9, 20], arr2 = [10, 12], [13, 15], 如果比较起点, arr1 比较一次以后就跑了


class Solution:
    def intervalIntersection(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] <= nums2[j][1] and nums2[j][0] <= nums1[i][1]:
                ans.append([max(nums1[i][0], nums2[j][0]), min(nums1[i][1], nums2[j][1])])
            if nums1[i][1] < nums2[j][1]: #为什么这里用位置1 比而不是0, 因为有可能nums1 跨度很大, 包括了多个nums2 的interval
                i += 1
            else:
                j += 1
                
        return ans