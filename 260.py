__author__ = 'lyb-mac'
import operator
def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        num = list(set(nums))
        for i in num:
            nums.pop(nums.index(i))
            if not i in nums:
                a.append(i)
        return a
        #my bad solution

        count = collections.Counter(nums)
        return [i for i,k in count.items() if k<2]
singleNumber([1,2,3])