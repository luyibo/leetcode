__author__ = 'user'
def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)/2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
print findMin([4,5,6,7,1,2,3])