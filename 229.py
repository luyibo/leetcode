__author__ = 'user'
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #boyer-moore majority vote alogrithm
        number1 = nums[0]
        number2 = nums[0]
        count1 = 0
        count2 = 0
        if len(nums)==0: return []
        for n in nums:
            if n==number1:
                count1 +=1
            elif n==number2:
                count2 +=1
            elif count1 == 0:
                number1,count1 = n,1
            elif count2 == 0:
                number2,count2 = n,1
            else:
                count1,count2 = count1-1,count2-1
        count1,count2 = 0,0
        for i in nums:
            if i ==number1:
                count1 +=1
            if i ==number2:
                count2+=1
        d = {number1:count1,number2:count2}
        print number1,number2
        return [x for x in d if d[x]>len(nums)/3]

print majorityElement([1,3,3,4])