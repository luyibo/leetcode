__author__ = 'lyb-mac'
def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a=[0]
        for i in range(n):
            a.extend([x + 2**i for x in a[::-1]])
        return a