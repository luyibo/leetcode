__author__ = 'user'
def searchRange( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        res = [-1,-1]
        while left<right:
            mid = (left+right)/2
            if target>nums[mid]:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return res
        res[0] = left
        right = len(nums)-1
        while left<right:
            mid = (left+right)/2+1
            if target<nums[mid]:
                right = mid - 1
            else:
                left = mid
        res[1] = right
        return res
print searchRange([2,2],2)