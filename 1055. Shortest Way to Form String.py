
题目, 给一个source string , 和一个target string, 问source string 的subsequence, 能否组成target string

问 需要重复source string 几次,
source = 'abc' target = 'abcab'
返回2, 因为target 可以由 两次source 组成



解法:
建造有限状态机(我tm也不知道为啥叫这个名字), 就是对于每个位置, 列出a~z 的下一位的idx, 
然后从source 的0位开始, idx track target 字母的位置, 如果source 里找到target 当前字母, 那么就到下一位去
Time: n + m
https://www.youtube.com/watch?v=UfmEfj3vRtE


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        next = [[-1] * 26 for _ in range(len(source) + 1)]
        n = len(source)
        source = '#' + source
        
        for i in range(n - 1, -1, -1):
            for k in range(26):
                next[i][k] = next[i + 1][k]
            next[i][ord(source[i + 1]) - ord('a')] = i + 1
            #这里next 数组next[i][:] 与next[i+1][:] 应该是完全一样的, 除了next[i][i+1 这一位的字母需要更新] = i+1
        
        j = 0 #stand position at source
        idx = 0 #idx for  target
        ans = 1 #至少走一遍
        
        while idx < len(target):
            if next[j][ord(target[idx]) - ord('a')] != -1:
                j = next[j][ord(target[idx]) - ord('a')]
                idx += 1
            else:
                if j == 0: #stand at 0, but not able find any target[idx]
                    return -1
                j = 0
                ans += 1
        return ans
		
解法2: 预处理 + 二分
思路就是对于每一个字母做一个inverted_idx, 这样每个字母出现的位置都被保留成了一个排好序的数组

然后遍历target ,

	if 找到当前ch 出现在dict里, 
		把当前字母的有序idx数组拿出来, 用现在的位置放进这个数组做binsect_left. 
		if 返回的位置小于有序数组的长度
			更新当前位置=有序数组[返回位置] + 1
		else:
			说明已经遍历完成, 找不到了, 必须从数组头开始重新查找
			ans += 1
			更新当前位置=有序数组[0] + 1
		
	else:
		return -1
		
		
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_idx = defaultdict(list)
        for i, ch in enumerate(source):
            inverted_idx[ch].append(i)
        
        ans = 1
        idx = -1
        
        for ch in target:
            if ch not in inverted_idx:
                return -1
            idx_of_ch = inverted_idx[ch]
            next_idx = bisect_left(idx_of_ch, idx)
            if next_idx == len(idx_of_ch):
                ans += 1
                idx = idx_of_ch[0] + 1
            else:
                idx = idx_of_ch[next_idx] + 1
        
        return ans
        