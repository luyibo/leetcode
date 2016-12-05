class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        basic = [0 for i in range(rowIndex+1)]
        basic[0] = 1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                basic[j] += basic[j-1]
        return basic

s = Solution()
print s.getRow(1)