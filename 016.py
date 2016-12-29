class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        flag = float('inf')
        if len(nums)<3:
            return 0
        for i in range(len(nums)):
            j = i+1
            l = len(nums)-1
            while j<l:
                s = nums[i]+nums[j]+nums[l]
                if s==target:
                    return target
                elif s>target:
                    l -= 1
                else:
                    j += 1
                if abs(s-target)<abs(flag):
                    flag = s-target
        return flag+target

s = Solution()
print s.threeSumClosest([1,1,1,0],100)