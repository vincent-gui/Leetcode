一番操作后, 如果回原点, 可以, 如果不在原点, 方向和初始方向相同, 不可以, 不同就可以


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        
        for ins in instructions:
            if ins == 'L':
                direction = (direction + 3) % 4 
            elif ins == 'R':
                direction = (direction + 1) % 4
            else:
                x += directions[direction][0]
                y += directions[direction][1]
                
        
        return (x, y) == (0, 0) or direction != 0