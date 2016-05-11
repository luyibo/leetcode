__author__ = 'lyb-mac'
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = list(set(nums))
        for i in temp:
            if nums.count(i)>(len(nums)/2):
                return i