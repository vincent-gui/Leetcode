class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        checking = []
        
        for num, start, end in trips:
            checking.append([start, num])
            checking.append([end, -num]) #为了防止当前点有上有下超出max， 采取先下后上的原则， 下车为负， 上车为正， 之后直接+= 就可以
            
        checking.sort()
        
        mx = 0
        for pos, cap in checking:
            mx += cap
            if mx > capacity:
                return False
        
        return True