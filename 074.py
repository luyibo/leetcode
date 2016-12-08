class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        row, col = len(matrix), len(matrix[0])
        end = row * col - 1
        while start <= end:
            mid = (start + end) / 2
            num = matrix[mid / row][mid % col]
            if num == target:
                return True
            elif num > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

s = Solution()
print s.searchMatrix([[3]],3)