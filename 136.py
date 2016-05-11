__author__ = 'lyb-mac'

def singleNumber( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums))*2)-sum(nums)