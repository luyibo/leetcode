class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        if len(nums)<4:
            return res
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:continue
                k = j+1
                p = len(nums)-1
                while k<p:
                    if k>j+1 and nums[k]==nums[k-1]:
                        k += 1
                        continue
                    if nums[i]+nums[j]+nums[k]+nums[p]==target:
                        res.append([nums[i],nums[j],nums[k],nums[p]])
                        k += 1
                        p -= 1
                    elif nums[i]+nums[j]+nums[k]+nums[p]>target:
                        p -= 1
                    else:
                        k += 1
        return res

s = Solution()
print s.fourSum([-2,0,-1,0,1,2],0)