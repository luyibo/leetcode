__author__ = 'user'
def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        min = nums[0]
        for num in nums:
            if num<min:
                min = num
        return min

def findMin2(nums):
    left = 0
    right = 0
    while left<right:
        mid = (left+right)/2
        if nums[mid]>nums[right]:
            left = mid + 1
        elif nums[mid]<nums[right]:
            right = mid
        else:
            if nums[mid] == nums[left]:
                left += 1
                right -= 1
            else:
                right = mid
    return nums[left]

print findMin([3,3,1,3])


