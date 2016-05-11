__author__ = 'lyb-mac'

def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        a,b=1,2
        for i in range(n-2):
            a,b=b,a+b
        return b