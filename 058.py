__author__ = 'lyb-mac'
def lengthOfLastWord(self, s):

        t = s
        if s=='':return 0
        count = 0
        while s[-1]==' ':
            s=s[:-1]
            if len(s)==0:return 0
        for i in s[::-1]:
            if i == ' ':
                return count
            count = count+1
        return len(s)