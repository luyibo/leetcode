__author__ = 'user'
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = (len(nums)+1)*len(nums)/2
        for i in nums:
            sum1 += 1
        return sum2-sum1

print missingNumber([2,0])