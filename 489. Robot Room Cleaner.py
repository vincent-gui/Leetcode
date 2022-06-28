
题目: 房间有个机器人, 机器人不知道房间多大, 也不知道具体坐标, 问设计一个算法, 用4个API 把房间打扫清楚
注意 move 的func 如果可以移动, 会按照现在的方向前进一步

解法dfs, 注意dfs 需要传入direction, 因为如果每次都是默认的方向, 就会导致, 上上上右上这样的, 
但是需要右保持直到全部右不可以走通


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] #这个顺序不能变,上,右下左
class Robot:
    
    def __init__(self, ):
        self.room = [[1, 1, 0, 1],[1,1,1,0],[1,1,0,1],[1,1,1,1,]] 
        self.x = 1
        self.y = 1
        self.n = len(self.room)
        self.m = len(self.room[0])
        self.dir = 0
        
    def move(self):
        dir = self.dir
        x = self.x
        y = self.y
        dx, dy = x + directions[self.dir][0], y + directions[self.dir][1]
        if dx <0 or dy <0 or dx >= self.n or dy >= self.m or self.room[dx][dy] == 0:
            return False
        self.x, self.y = dx, dy
        return True
        

    def turnRight(self):
        self.dir = (self.dir + 1) % 4


    def clean(self):
        self.room[self.x][self.y] = '#'



class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def backTrack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        
        def dfs(x, y, direct): 
		#这里需要传进一个方向的, 因为如果每次都是默认的方向, 就会导致, 上上上右上这样的, 
		#但是需要右保持直到全部右不可以走通
            if (x, y) in seen:
                return 
            seen.add((x, y))
            robot.clean()
            for _ in directions:
                if robot.move():
                    print(directions[direct])
                    dx, dy = x + directions[direct][0], y + directions[direct][1]
                    dfs(dx, dy, direct)
                    backTrack()
                robot.turnRight()
                direct = (direct + 1 ) % 4
        seen = set()
        dfs(1, 1, 0)

                
        

r = Robot()
Solution().cleanRoom(r)
print(r.room)