__author__ = 'user'
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i,num in enumerate(numbers):
            if target - num in result:
                return [result[target-num]+1,i+1]
            result[num] = i

    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while start<end:
            total = numbers[start]+numbers[end]
            if total==target:
                return [start+1,end+1]
            if total>target:
                end -=1
            else:
                start +=1
enumerate

s = Solution()
print s.twoSum([-3,3,4,90],0)