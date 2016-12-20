__author__ = 'user'
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            elif target> nums[mid]:
                left = mid+1
            else:
                right = mid-1
        if target>nums[left]:
            return left+1
        return left

s = Solution()
print s.searchInsert([1,3,5,6],1)