__author__ = 'lyb-mac'

def moveZeroes( nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''a = nums.count(0)
        for i in range(a):
            nums.remove(0)
            nums.append(0)'''
        count = 0
        c = 0
        t = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                count += 1
                nums.append(0)
        while c<count:
            if nums[t]==0:
                del nums[t]
                c +=1
            else:
                t += 1
        print nums
moveZeroes([0,0,1,3,0,4])