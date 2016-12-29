__author__ = 'lyb-mac'

def containsNearbyDuplicate( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        a = {}
        for i in range(len(nums)):
            if not nums[i] in a:
                a[nums[i]]=i
            else:
                return i-a[nums[i]]<=k
        return False
print containsNearbyDuplicate([-1,-1],1)