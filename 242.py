__author__ = 'lyb-mac'
from collections import Counter
def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''a = Counter(s)
        b = Counter(t)
        return a==b'''
        a  = {}
        b = {}
        if len(s)!=len(t):return False
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:a[s[i]] = a[s[i]]+1
        for i in range(len(t)):
            if t[i] not in b:
                b[t[i]] = 1
            else:b[t[i]] = b[t[i]]+1
        return a==b

print isAnagram('a','b')
