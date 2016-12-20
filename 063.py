__author__ = 'user'
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        minpath = [0]*len(obstacleGrid[0])
        minpath[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    minpath[j] = 0
                elif j>0:
                    minpath[j] += minpath[j-1]
        return minpath[-1]
s = Solution()
s.uniquePathsWithObstacles([[0],[1]])