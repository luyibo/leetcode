def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    '''r = [0]*len(nums)
    result = []
    for i in range(len(nums)):
        print i
        if r[nums[i]-1] == 0:
            r[nums[i]-1] = nums[i]
        else:
            result.append(nums[i])
    return result'''
    r = []
    for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index]>0:
                nums[index] = -(nums[index])
                print nums
            else:
                r.append(abs(nums[i]))
                print r
l = [4,3,2,7,8,2,3,1]
findDuplicates(l)