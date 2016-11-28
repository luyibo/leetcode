__author__ = 'lyb-mac'
def isHappy( n):
        """
        :type n: int
        :rtype: bool
        """

        l = []
        while n!=1:
            if n in l:return False
            l.append(n)
            n = sum([int(i)**2 for i in str(n)])
            print n
        return True


isHappy(7)