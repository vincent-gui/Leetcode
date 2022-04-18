题目: 给一个数组, 求是否存在连续subarray 的和可以被k 整除

思考, 一开始按照subarry sum == k 做的, 方向错了, 
	因为 (a + b) % c = (a % c + b % c ) % c, 就是说即使 0 ...i ....j中, 应该要找的是   如果sum(0~i) % k 等于sum(0~j) % k
	也就意味着 sum(i~j) % k 等于0
解法: 
	那么只需要把所有的cumSum % k存起来, 如果不在hash map 里, 把idx 存起来, 如果在map 里, 则查找 i - 以前存储的idx >= 2
	
	特殊处理{0:-1} 例子[3, 3] k = 6, 因为第二个三的时候, cum 是6, idx 是1, 这个时候需要补充一个-1 才能满足条件


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: -1} # save prefix and idx
        tmp = 0
        
        for i, num in enumerate(nums):
            #using num update d
            tmp += num
            if tmp % k not in d:
                d[tmp % k] = i
            else:
                if i - d[tmp % k] >= 2:
                    return True
        return False