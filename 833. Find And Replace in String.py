题目: 给了一个字符串, 一个source, 一个target, 还有一个indexs 数组, 
问如果在index 数组里给的那个数, 和s里以idx 开始的等于source 里source[idx] 相等, 那么替换为target[idx] 的字符

这个题真不咋样


思路是从右到左, 这样不会因为被target[idx] 替换后导致s的长度变化
又因为 indices 的长度, sources 的长度, 和targets 的一样,直接zip 在一起就好了

class Solution:
    def findReplaceString(self, string: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indices, sources, targets), reverse=True):
            string = string[:i] + t + string[i + len(s):] if string[i: i + len(s)] == s else string
					#前半段不变的, t 表示target[idx], string[i + len(s):] 表示后半段剩余的部分
        
        return string
		
		
		