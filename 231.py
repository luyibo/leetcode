__author__ = 'lyb-mac'
import math
def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #my
        if n<=0:return False
        temp = math.log(n,2)
        if(abs(temp-round(temp)))<=0.00000000001:
            return True
        return False
        #excellent
        return n&-n==n and n!=0
