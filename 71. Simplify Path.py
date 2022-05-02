题目: 
	1. '.' 表示当前目录, 题目里需要直接跳过 (遇到'.' 直接skip)
	2. '..' 表示父目录, 也就意味着, 如果stack存在,  遇到'..', 那么需要从stack 里pop 出last 的item 
	3. 多个斜杠 '/////', 需要当成一个斜杠处理, (因为整个需要以'/' split, 所以都被取消掉, 最后用'/'.join就会treat 成单个'/'
	4. 多个点 '.....' 当成文件名处理 (正常多个....., 直接放进stack)
	5. 文件需要以一个单斜杠开始, 不能以'/' 结尾
	
思路: 
	先用 '/' split 整个, 然后判定, 
		1.如果.. 并且stack 有, 则pop, 
		2. 否则(else) 如果不是., 也不是空就入栈
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_list = path.split('/')
        for item in path_list:
            if item == '..':
                if stack:
                    stack.pop()
            elif item != '.' and item != '':
                stack.append(item)
        
        return '/' + '/'.join(stack)