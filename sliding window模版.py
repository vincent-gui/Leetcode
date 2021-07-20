class Solution(object):
    def slidingWindow(self, s):
        """
        :type s: str
        :rtype: int
        07/20
        """
        
        seen = {} #dict 追踪看过的字符, {'letter': index}
        ans = 0 #track result
		start = 0 #起始的慢指针, 在sliding window 里这个指针永远不能回撤
        for i, letter in enumerate(s):
		
			#case 1
            if letter in seen:
                prev_idx = seen[letter]
                start = max(prev_idx + 1, start)
				
			#case 2
			if len(seen) > k:
                mi_k, mi_v = None, len(s) + 1
                for k, v in seen.items():
                    if v < mi_v:
                        mi_k = k
                        mi_v = v
                start = mi_v + 1
                del seen[mi_k]
				
			#update 	
            seen[letter] = i #更新最新的letter:index 映射关系, 有时候在循环的第一步, 有时候在最后
            ans = max(i - start + 1, ans)
        
        return ans
                