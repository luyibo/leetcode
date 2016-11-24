__author__ = 'user'
def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums)==0:return []
    mark = []
    result = []
    start = 0
    for i in range(len(nums)-1):
        
        if nums[i]+1==nums[i+1]:
            continue
        else:
            mark.append(i)
    for i in mark:
        if start == i:
            result.append("%d"%nums[i])
        else:
            result.append("%d->%d"%(nums[start],nums[i]))
        start = i+1
    if nums[start]==nums[-1]:
        result.append("%d"%nums[start])
    else:
        result.append("%d->%d"%(nums[start],nums[-1]))
    print result
summaryRanges([])
