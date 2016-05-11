__author__ = 'lyb-mac'

def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:return False
        while '()' or '[]' or '{}' in s:
            t = s.replace('()','').replace('[]','').replace('{}','')
            print s
            if t==s:
                return False
            if t=='':
                return True
            s = t



print isValid('([])')