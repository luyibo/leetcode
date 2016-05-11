__author__ = 'lyb-mac'
def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(list(set(nums))*3)-sum(nums))/2