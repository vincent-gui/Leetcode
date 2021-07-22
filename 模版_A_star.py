'''
https://blog.csdn.net/hitwhylz/article/details/23089415
http://www-cs-students.stanford.edu/~amitp/gameprog.html#Paths
'''


class State:
    def __init__(self, g_in, f_in):
        self.g = g_in
        self.f = f_in

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        source = self.matrixToString(init_state)
        target = self.matrixToString(final_state)
        if not self.check(source, target):
            returnb -1
        open = {}
        close = set()
        open[source] = State(0, self.getH(source, target))
        
        while open:
            curr = self.findMin(open)
            if curr == target:
                return open[curr].g
            
            close.add(curr)
            
            for nxt in self.getNext(curr):
                if nxt not in close:
                    if nxt not in open or open[nxt].g > open[curr].g + 1:
                        open[nxt] = State(open[curr].g + 1, open[curr].g + 1 + self.getH(nxt, target))
            del open[curr]
        return -1
    def check(self, s, t):
        sc = list(s)
        tc = list(t)
        r1 = r2 = 0
        for i in range(9):
            for j in range(i):
                if sc[i] != '0' and sc[j] != '0' and sc[j] > sc[i]:
                    r1 += 1
                if sc[i] != '0' and sc[j] != '0' and tc[j] > tc[i]:
                    r2 += 1
        return r1 % 2 == r2 % 2

    def getNext(self, string):
        ans = []
        points = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        zeroIdx = string.index('0')
        x = zeroIdx / 3
        y = zeroIdx % 3
        
        for point in points:
            nx, ny = x + point[0], y + point[1]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            sc = list(string)
            sc[x * 3 + y] = sc[nx * 3 + ny]
            sc[nx * 3 + ny] = '0'
            ans.append(''.join(sc))
        
        return ans
            
        
        
        
    def findMin(self, open):
        out = ''
        minF = 999
        for key in open:
            if open[key].f < minF:
                minF = open[key].f
                out = key
        
        return out
       
    def matrixToString(self, matrix):
        out = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out += str(matrix[i][j])
        
        return out
    
    def getH(self, curr, target):
        out = 0
        for i in range(9):
            if target[i] != '0':
                idx = curr.index(target[i])
                cx = idx / 3
                cy = idx % 3
                
                tx = i / 3
                ty = i % 3
                out += abs(cx - tx) + abs(cy - ty)
        return out


init_state = [[1,2,3],[4,5,6],[7,8,0]]
final_state=[[1,2,3],[4,5,6],[8,7,0]]
print Solution().minMoveStep( init_state, final_state)