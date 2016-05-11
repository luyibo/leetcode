__author__ = 'lyb-mac'

def countBits( num):
        """
        :type num: int
        :rtype: List[int]
        """
        print [bin(i)[2:].count('1') for i in range(num)]

countBits(5)