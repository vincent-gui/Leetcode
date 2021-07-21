#track sliding window内部数量的方法
1. cnt += 1 then match cnt == len(target)
2. i - start + 1 > len(target)


#valid 和与match logic 的关系
#如果出现valid, 也就意味着问题是求最短substring 一类的, 那么在做match 的时候需要去match len(seen)
#没有valid 的时候要match len(target)

class Solution(object):
    def slidingWindow(self, s, target):
        """
        :type s: str
        :rtype: int
        07/20
        """
        
        seen = {} #dict 追踪target里的字符, {'letter': index}
		for letter in target:
			seen[letter] = seen.get(letter, 0) + 1
        ans = 0 #track result
		start = 0 #起始的慢指针, 在sliding window 里这个指针永远不能回撤
		#valid = 0
		check = {} #slidingWindow
        for i, letter in enumerate(s):
		
			#case 1 match logic  LC 3
            if letter in check:
                prev_idx = check[letter]
                start = max(prev_idx + 1, start)
				
			#case 2 match logic 的关系 lc 159, 340
			if len(check) > k:
                mi_k, mi_v = None, len(s) + 1
                for k, v in check.items():
                    if v < mi_v:
                        mi_k = k
                        mi_v = v
                start = mi_v + 1
                del check[mi_k]
				
			#update 	
            check[letter] = i #更新最新的letter:index 映射关系, 有时候在循环的第一步, 有时候在最后
            ans = max(i - start + 1, ans)
        
        return ans
                