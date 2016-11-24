__author__ = 'user'
def productExceptSelf( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = 1
        count = 0
        s = 1
        for i in nums:
            r *= i
            if i==0:
                count +=1
                continue
            s *= i
        if r == 0:
            if count > 1:
                return [0]*len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = s
                else:
                    nums[i] = 0
            return nums
        return [r/x for x in nums]

print productExceptSelf([1,0])