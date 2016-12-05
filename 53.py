__author__ = 'user'
def maxSubArray( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nstart = nums[-1]
        nall = nums[-1]
        for num in nums[-2::-1]:
            if nstart < 0 :
                nstart = 0
            nstart += num
            if nstart > nall:
                nall = nstart
        return nall

print maxSubArray([-2,-1,-2])