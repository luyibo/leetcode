__author__ = 'user'
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        minipath = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            minipath[0][i] = 1
        for j in range(m):
            minipath[j][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                minipath[i][j] = minipath[i-1][j] + minipath[i][j-1]
        return minipath[-1][-1]
    def unique(self,m,n):
        minpath = [0 for i in range(n)]
        minpath[0] = 1
        for i in range(m):
            for j in range(1,n):
                minpath[j] += minpath[j-1]
        return minpath[-1]
s = Solution()
print s.uniquePaths(3,7)
print s.unique(3,7)