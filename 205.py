__author__ = 'lyb-mac'

def isIsomorphic( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(s)==len(t) and len(set(zip(s,t)))==len(set(s)) and len(set(s))==len(set(t))
