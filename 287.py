__author__ = 'user'
def findDuplicate( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for i in nums:
        sum |=i
        print sum
print findDuplicate([1,3,4,2,2])