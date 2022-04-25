题目: 要求实现一个randomset, 要求insert, remove, getrandom 都是O(1)

解法如下, 用一个dict 和一个array 去track 所有的item


class RandomizedSet:

    def __init__(self):
        self.nums = [] #num
        self.d = {} #num, idx
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.nums.append(val)
        self.d[val] = len(self.nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        last = self.nums[-1]
        last_idx = self.d[last]
        val_idx = self.d[val]
        self.d[last] = val_idx
        self.nums[val_idx] = last
        del self.d[val]
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]