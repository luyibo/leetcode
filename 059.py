__author__ = 'lyb-mac'
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        res = [[0 for i in range(n)]for i in range(n)]
        rowstart = 0
        colstart = 0
        rowend = n
        colend = n
        while rowstart<rowend and colstart<colend:
            for i in range(colstart,colend):
                res[rowstart][i] = num
                num += 1
            rowstart += 1
            for i in range(rowstart,rowend):
                res[i][colend-1] = num
                num += 1
            colend -= 1
            for i in range(colend-1,colstart-1,-1):
                res[rowend-1][i] = num
                num += 1
            rowend -= 1
            for i in range(rowend-1,rowstart-1,-1):
                res[i][colstart] = num
                num += 1
            colstart += 1
        return res

s = Solution()
print s.generateMatrix(3)


