题目: 就是给了一串log, 里面包括了time, userA, userB, 问, 最早什么时间所有人会都变成朋友, 如果没有则返回-1


Union find , 注意每次成功连接 self.cnt -= 1, 最后等于1 就意味着已经全部连接了
class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        mapping = {i: i for i in range(n)}
        self.cnt = n
        def find(node):
            path = []
            while node != mapping[node]:
                path.append(node)
                node = mapping[node]
                
            for n in path:
                mapping[n] = node
            return node
        
        def connect(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                mapping[root_a] = root_b
                self.cnt -= 1
        
        for log in sorted(logs):
            time, a, b = log 
            connect(a, b)
            if self.cnt == 1:
                return time
        
        return -1