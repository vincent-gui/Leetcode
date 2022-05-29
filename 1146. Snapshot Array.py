题目: 给一个大小, 然后对于给定的index 赋值val, 并且可以做snap, 每做一次snap, ID就会增长一次

brute force解法: 

init 一个list 长度为给定的长度, 然后每次snap 的时候复制一下
空间复杂度很大



看解说想出来的解法


解法1
以idx 为key, value: (snapid 和val) 的组合, idx 1 : [[0, 1], [2, 4], [2, 2], [7, 10]]

如果没找到key , 则返回0
否则返回key 的snap id 的最后一个值

class SnapshotArray:

    def __init__(self, length: int):
        self.index = defaultdict(list) #key: idx, val: list of verison  ,
        self.id = 0
        

    def set(self, index: int, val: int) -> None:
        self.index[index].append((self.id, val))
        
        

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        his = self.index[index]
        if len(his) == 0:
            return 0
        start, end = 0, len(his) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if his[mid][0] <= snap_id:
                start = mid
            else:
                end = mid
        if his[end][0] <= snap_id:
            return his[end][1] 
        if his[start][0] <= snap_id:
            return his[start][1]
        return 0
		
		
解法2:  针对于同一个snap 的同一个值被修改多次的情况, 直接覆盖而不是添加, 这样节省空间


class SnapshotArray:

    def __init__(self, length: int):
        self.map = defaultdict(list) #key: idx, val: list of verison
        self.id = 0
        

    def set(self, index: int, val: int) -> None:
        self.map[index].append((self.id, val))
        
        

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        his = self.map[index]
        if len(his) == 0:
            return 0
        start, end = 0, len(his) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if his[mid][0] <= snap_id:
                start = mid
            else:
                end = mid
        if his[end][0] <= snap_id:
            return his[end][1] 
        if his[start][0] <= snap_id:
            return his[start][1]
        return 0
        
        