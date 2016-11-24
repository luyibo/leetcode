__author__ = 'lyb'

def missingNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = [-1] * (len(nums)+1)
    for i in nums:
        l[i] = i
    print l
    for i in range(len(l)):
        if l[i] != i:
            return i
    return i + 1

print missingNumber([1,0])