


题目就是找到最长的subsequence. 长度相等选择letter 最小的
同1055, 792



class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        inverted_idx = defaultdict(list)
        def valid(word):
            curr = 0
            for ch in word:
                idx = bisect.bisect_left(inverted_idx[ch], curr)
                if idx >= len(inverted_idx[ch]):
                    return False
                curr = inverted_idx[ch][idx] + 1
            return True
        
        for i, ch in enumerate(s):
            inverted_idx[ch].append(i)
            
        ans = ''
        for word in dictionary:
            if valid(word):
                if len(ans) < len(word):
                    ans = word
                elif len(ans) == len(word) and word < ans:
                    ans = word
                
        
        return ans