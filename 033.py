class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            elif nums[mid]>=nums[start]:
                if target<nums[mid] and target>=nums[start]:
                    end = mid - 1
                else:start = mid + 1
            else:
                if target>nums[mid] and target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if nums[start] == target:
            return start
        else:return -1
s = Solution()
print s.search([1,3,1,1,1],3)