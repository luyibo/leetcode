__author__ = 'user'
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(grid[0])):
            grid[0][i] += grid[0][i-1]
        for j in range(1,len(grid)):
            grid[j][0] +=grid[j-1][0]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]


s = Solution()
print s.minPathSum([[2],[1]])