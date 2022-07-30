给了一个stirng, 里面包括了字母和数字

返回大小写的combaination

开一个ans=[''] 的结果集, 遇到字母, 就把这个翻倍, 然后分别append


time: O(2**n) 
space: O(2**n)


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for item in s:
            if item.isalpha():
                ans *= 2
                for i in range(len(ans) // 2):
                    ans[i] += item
                for i in range(len(ans)//2, len(ans)):
                    ans[i] += item.swapcase()
            else:
                for i in range(len(ans)):
                    ans[i] += item
        
        return ans


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