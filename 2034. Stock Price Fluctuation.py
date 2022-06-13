题目: 给了一串(时间, 股票价格), 可能会给出相同的时间, 不同的价格, 表示价格更正


.解法: stock 用hashtable 
miheap
mxheap 

如果和dict 里的比对相同则push 回去
否则跳过

一开始想的是一个单调stack, 其实不需要



class StockPrice:

    def __init__(self):
        self.stock = {}
        self.minHeap = []
        self.maxHeap = []
        self.curr_time = -1
        

    def update(self, timestamp: int, price: int) -> None:
        self.stock[timestamp] = price
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (-price, timestamp))
        self.curr_time = max(self.curr_time, timestamp)
        
        

    def current(self) -> int:
        return self.stock[self.curr_time]
        

    def maximum(self) -> int:
        mxHeap = self.maxHeap
        while mxHeap:
            price, ts = heapq.heappop(mxHeap)
            if self.stock[ts] == -price:
                heapq.heappush(mxHeap, (price, ts))
                return -price
            
        

    def minimum(self) -> int:
        miHeap = self.minHeap
        while miHeap:
            price, ts = heapq.heappop(miHeap)
            if self.stock[ts] == price:
                heapq.heappush(miHeap, (price, ts))
                return price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()