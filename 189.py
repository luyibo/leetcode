__author__ = 'lyb-mac'

def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''k = k%len(nums)
        temp = nums[:-k]
        nums.extend(temp)
        del nums[:len(temp)]'''
        nums[:] = nums[-k:] + nums[:-k]
rotate([1,2],1)
