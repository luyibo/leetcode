def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    '''r = []
    result = [0]*len(nums)
    print nums
    for i in range(len(nums)):
        result[nums[i]-1] = nums[i]

    for i in range(len(result)):
        if result[i]==0:
            r.append(i+1)
    print r'''
    r = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])
        print nums
    for i in range(len(nums)):
        if nums[i]>0:
            r.append(i+1)
    print r
l = [4,3,2,7,8,2,3,1]

findDisappearedNumbers(l)
