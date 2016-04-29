__author__ = 'lyb-mac'
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(list(set(nums)))!= len(nums):
            return True
        else:return False
