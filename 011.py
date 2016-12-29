class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(min(height[left], height[right]) * (right - left), area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

s = Solution()
s.maxArea([2,3,4,5,18,17,6])