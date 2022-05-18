题目: 给一个矩阵, 然后1 表示房子, 问在途中选取一个点到 所有房子距离最近
表示房子的点也可以选择


解法: 一开始是用所有的房子做bfs, 时间复杂度其实是m 平方乘以 n平方

因为其实图上的每个点都可以见面, 不像 (317. Shortest Distance from All Buildings) 里面有些格子并不可以见面, 那么这个题就简单一些

假设所有的点在都在x轴上, 那么离所有点距离和 最近的点一定是中点(median), 同样适用于y轴, 

所以扫描所有的点, 把x轴和y轴坐标分别放进两个数组, 并且排序, 对两个数组找中点, 这样的(median_x, median_y) 其实就是那个要找的点, 最后对于所有的x 和y 分别求曼哈顿距离就可以了





class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        x_points, y_points = [], []
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x_points.append(i)
                    y_points.append(j)
        
        x_points.sort()
        y_points.sort()
        median_x, median_y = x_points[len(x_points) // 2], y_points[len(y_points) // 2]
        
        ans = 0
        for x in x_points:
            ans += abs(median_x - x)
            
        for y in y_points:
            ans += abs(median_y - y)
            
        return ans