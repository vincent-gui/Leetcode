解法: 两个指针, 一个指向外面, 一个指向里面, 并且要注意内部的空集

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.outer = 0
        self.inner = 0
        self.arr = vec
        

    def next(self) -> int:
        if self.hasNext():
            out = self.arr[self.outer][self.inner]  #这里千万注意, 最外层写在外面
            self.inner += 1
            return out
        

    def hasNext(self) -> bool:
        while self.outer < len(self.arr):
            while self.inner < len(self.arr[self.outer]):
                return True
            self.outer += 1
            self.inner = 0
        
        return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()