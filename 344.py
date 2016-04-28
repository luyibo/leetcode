__author__ = 'lyb-mac'
def reverse(s):
        a=[]
        for i in range(len(s)-1,-1,-1):
            a.append(s[i])
        print ''.join([i for i in a ])
reverse('abc')