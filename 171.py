__author__ = 'lyb-mac'
def titleToNumber( s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        temp = len(s)
        i = 0
        while temp>0:
            sum = sum+(ord(s[i])-64)*26**(temp-1)
            temp = temp-1
            i = i+1
        return sum
print titleToNumber('BA')