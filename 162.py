__author__ = 'user'
#coding=utf-8
def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        首先我们找到中间节点mid，如果大于两边返回当前的index就可以了，
        如果左边的节点比mid大，那么我们可以继续在左半区间查找，
        这里面一定存在一个peak，为什么这么说呢？假设此时的区间范围为[0,mid-1]
        ，因为num[mid-1]一定大于num[mid]，如果num[mid-2]<=num[mid-1]，
        那么num[mid-1]就是一个peak。如果num[mid-2]>num[mid-1]，
        那么我们就继续在[0,mid-2]区间查找，因为num[-1]为负无穷，
        所以我们最终绝对能在左半区间找到一个peak。同理右半区间一样。'''
        '''peak = 0
        flag = 0
        maxium = -float('inf')
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                peak = nums[i-1]
                if peak>maxium:
                    maxium = peak
                    flag = i-1
            elif nums[i]>nums[i-1]:
                peak = nums[i]
                if peak>maxium:
                    maxium = peak
                    flag = i
        return flag'''
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)/2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
print findPeakElement([1,7,3,4,5,1,2,3,4])