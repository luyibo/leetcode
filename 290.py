__author__ = 'lyb-mac'

def wordPattern( pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(str.split())!=len(pattern):return False
        str1 = str.split()
        if len(set(str1))!=len(set(pattern)):return False
        return len(set(zip(str1,pattern)))==len(set(pattern))


print wordPattern('syys','a abc abc a')