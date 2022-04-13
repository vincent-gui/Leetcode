这个题 其实就是寻找两个linkedin list 第一个相同的node

p1 -> p2 -> p3 -> c1 -> c2 -> c3

d1 -> c1 -> c2 -> c3

相同公共点就是c1, 其实如果以p1 和 d1 分别为开始, 走完两个链表, 那么他们的总路径相同, 一定会在第一个相同的node 相遇

p1 -> p2 -> p3 -> c1 -> c2 -> c3 -> d1 -> c1 -> c2 -> c3

d1 -> c1 -> c2 -> c3 -> p1 -> p2 -> p3 -> c1 -> c2 -> c3

所以这个就是解法


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p1, q1 = p, q
        while p != q:
            p = p.parent if p.parent else  q1
            q = q.parent if q.parent else p1
        
        return p