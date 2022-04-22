题目: 一个grid, 里面有陆地, 求陆地面积


解法: 只考虑左侧和上侧的格子, 遇到格子就+ 4, 如果上面有土地就-2, 如果左侧有也-2


follow up, 如果有多个land ,怎么求最大, 怎么求最小


public class Solution {
    public int islandPerimeter(int[][] grid) {
        if (grid == null) return 0;
        for (int i = 0 ; i < grid.length ; i++){
            for (int j = 0 ; j < grid[0].length ; j++){
                if (grid[i][j] == 1) {
                    return getPerimeter(grid,i,j);
                }
            }
        }
        return 0;
    }
    
    public int getPerimeter(int[][] grid, int i, int j){
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {return 1;}
        if (grid[i][j] == 0) {
            return 1;
        }
        if (grid[i][j] == -1) return 0;
        
        int count = 0;
        grid[i][j] = -1;
        
        count += getPerimeter(grid, i-1, j);
        count += getPerimeter(grid, i, j-1);
        count += getPerimeter(grid, i, j+1);
        count += getPerimeter(grid, i+1, j);
        
        return count;
        
    }
}

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 4
                    if i and grid[i-1][j] == 1:
                        ans -= 2
                    if j and grid[i][j - 1] == 1:
                        ans -= 2
        return ans