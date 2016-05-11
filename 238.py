__author__ = 'lyb-mac'
import operator
def productExceptSelf( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = reduce(operator.mul,nums)
        if total==0:
            temp = nums.index(0)
            nums.pop(nums.index(0))
            total = reduce(operator.mul,nums)
            if total==0:
                return [0]*(len(nums)+1)
            else:
                a = [0]*len(nums)
                a.insert(temp,total)
                return a
        return [total/i for i in nums]

print productExceptSelf([1,0])