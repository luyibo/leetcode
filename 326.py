__author__ = 'lyb-mac'

import math
def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:return False
        temp = math.log(n,3)
        if abs(temp-round(temp))<0.0000000000001:
            return True
        return False
