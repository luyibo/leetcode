__author__ = 'user'
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min = nums[0]
        Max = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num<0:
                Max,Min = Min,Max

            Max = max(Max*num,num)
            Min = min(Min*num,num)
            result = max(result,Max)
        return result

s = Solution()
print s.maxProduct([-2,0,-1,1,-5,-1])