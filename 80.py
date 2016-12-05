class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:

            if i >= 2 and num != nums[i - 2]:
                nums[i] = num
                i += 1
            if i < 2:
                nums[i] = num
                i += 1
        return i