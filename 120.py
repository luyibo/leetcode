class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:return
        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res = min(res[j],res[j+1])+triangle[i][j]
        return res

    def get_min(self,row,col,triangle):
        res = min(self.get_min([row+1],[col],triangle),
                  self.get_min([row+1],[col+1],triangle)
                  ) + triangle[row][col]
