class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        self.dfs([], ans, s, n)
        return ans
        
    def dfs(self, tmp, ans, s, n):
        if sum([len(item) for item in tmp]) == n:
            ans.append(tmp[:])
            return
        for i in range(len(s)):
            if self.is_match(s[:i+1]):
                tmp.append(s[:i+1])
                self.dfs(tmp, ans, s[i+1:], n)
                tmp.pop()
        
    def is_match(self, string):
        if not string:
            return False
        start, end = 0, len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True