class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for num in nums:
            if num == 2:
                count += 1
        l = len(nums)
        i = 0
        while i < l-count:
            if nums[i] == 0:
                nums.insert(nums.pop(i), 0)
            elif nums[i] == 2:
                nums.append(nums.pop(i))
                i -= 1
            i += 1
        return nums

s = Solution()
print s.sortColors([2,1,2,1,0,0,0])