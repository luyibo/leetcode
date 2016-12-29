__author__ = 'user'
def findDuplicate( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    right = len(nums)-1
    while left<=right:
        cnt = 0
        mid = (right-left)/2
        for num in nums:
            if mid>=num:
                cnt += 1
        if cnt>mid:
            right = mid - 1
        else:left = mid + 1
    return left

def find(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow==fast:
            slow = 0
            while slow!=fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow

print find([1,2,1,4,5,3])