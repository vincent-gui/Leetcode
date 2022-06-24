
题目: 给了一串长度相同的字符串, 问是否有两个字符串, 有且仅有一个相同的idx 上的字母不同
例如 'abcd', 'aacd' idx等于1的位置上, 字母不同, 剩余所有位置字母相同

思路: 考虑到这个问题, 如果暴力解法就是n*n*m, 每个字符串两两相比较

有没有办法降低到 n*m

对于每个字符串编码, 26进制编码, 类似于2进制,  'abcd' 相当于'0123', 转换的方式是 hash[i] = (0 * 26**3) + (1 * 26**2) + (2 * 26**1) + (3 * 26**0)

对于每一个位置进行消去, 消去就是 hash[i] - (当前位置字母 * 26 ** 几次方)

这个题的写法上也有一些巧妙地地方, 值得学习

class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        hashes = [0] * n 
        MOD = 10 ** 11 + 7
        base = 26
        for i in range(n):
            for j in range(m):
                hashes[i] = (26 * hashes[i] + (ord(dict[i][j]) - ord('a'))) % MOD
        
        power = 1
        for j in range(m - 1, -1, -1):
            seen = set()
            for i in range(n):
                new_hash = (hashes[i] - (ord(dict[i][j]) - ord('a')) * power) % MOD
                if new_hash in seen:
                    return True
                seen.add(new_hash)
            power = power * base % MOD #注意这里需要再次mod , 否则会太大
        
        return False
                