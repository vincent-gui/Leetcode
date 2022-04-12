解法就是基于\n 做分层

特殊的test case "dir\n        file.txt", 表示dir 根目录, 和 '        file.txt' 在同一个层级

方法1, 是用dict 记录每一层 的深度, 最后loop 所有比key 小的 做sum
方法二就是每一层更新, 每一层记录的是so far 的深度, 这样不需要back track 别的深度

方法1
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input_list = input.split('\n')
        
        d = {}
        ans = 0
        
        for item in input_list:
            if '.' not in item:
                key = item.count('\t')
                value = len(item.replace('\t', ''))
                d[key] = value
            else:
                key = item.count('\t')
                length = sum(d[k] for k in d.keys() if k < key) + key + len(item.replace('\t', ''))  #注意这里需要只考虑比key 小的, 因为有可能别的层的很深, dict 小于key 的才会被update
                ans = max(ans, length)
        
        return ans
    

方法2
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        # The splitlines() method splits a string into a list. The splitting is done at line breaks
        # The lstrip() method removes any leading characters (space is the default leading character to remove)
        # string.lstrip(characters) -> characters = A set of characters to remove as leading characters
        # For strings with special escape characters (they are prefixed by a backslash(\), only the character is counted towards the length and not the backslash. Examples include (\n, \t, \', etc)
        
        maxLength = 0
        pathLength = {0 : 0}
        l = input.splitlines()
        for line in l:
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            
            if "." in name:
                maxLength = max(maxLength, pathLength[depth] + len(name))
            else:
                pathLength[depth + 1] = pathLength[depth] + len(name) + 1
        
        return maxLength
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Solution().lengthLongestPath(input)	