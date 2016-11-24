__author__ = 'user'
def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums)==0:
            return -float('inf')
        if len(nums)<=2:
            return max(nums)
        l = [-float('inf')]*3
        for i in nums:
            if i >l[0]:
                l[0],l[1],l[2] = i,l[0],l[1]
            elif l[0]>i>l[1]:
                l[1],l[2] = i,l[1]
            elif l[1]>i>l[2]:
                l[2] = i
            print l

nums = [2,2,3,1]

print thirdMax(nums)
