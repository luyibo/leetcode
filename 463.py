class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land = 0
        neighbour = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
                    if i<len(grid)-1 and grid[i+1][j] == 1:neighbour += 1
                    if j<len(grid[0])-1 and grid[i][j+1] == 1:neighbour += 1
        return land*4-neighbour*2

s = Solution()
s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])