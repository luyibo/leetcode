__author__ = 'lyb-mac'
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        number = nums[0]
        count1 = 0
        for i in nums:
            if number == i:
                count +=1
            else:
                count -=1
            if count == 0:
                number,count = i,1
        for i in nums:
            if i == number:
                count1 +=1
        if count1>len(nums)/2:
            return number