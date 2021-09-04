
总结：

考察逻辑思维

从左到右， cele 为0，循环1~n

如果cele 认识i， 说明cele 不行， 但是i 有可能行

结束这个循环后， cele 后面的已经被验证过， cele 不认识后边的

但是可能后边的也不认识cele，cele 之前的也有可能不认识cele 或者cele 认识前面的

所以需要再次从头循环到尾
当 j ！= cele， 但是j 不认识cele 或者cele 认识j 直接返回-1

最后返回cele

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        
        for i in range(n):
            if i != celebrity and knows(celebrity, i):
                return -1
            if i != celebrity and not knows(i, celebrity):
                return -1
        
        return celebrity