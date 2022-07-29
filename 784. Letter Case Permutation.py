给了一个stirng, 里面包括了字母和数字

返回大小写的combaination

time: O(2**n) 
space: O(2**n)

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(s, idx, substr):
            if idx == len(s):
                ans.append(substr[:])
                return
            if s[idx].isalpha():
                for letter in [s[idx].upper(), s[idx].lower()]:
                    substr += letter
                    dfs(s, idx + 1, substr)
                    substr = substr[:-1]

            else:
                substr += s[idx]
                dfs(s, idx + 1, substr)
                substr = substr[:-1]

        ans = []
        dfs(s, 0, '')
        
        return ans