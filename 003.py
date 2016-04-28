__author__ = 'lyb-mac'

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        a = []
        b = []
        for i in range(len(s)):
                if(s[i] not in a):
                    a.append(s[i])
                else:
                    a.append(s[i])
                    if (len(a)>len(b)):
                        b = a[:-1]
                    a = a[a.index(s[i])+1:]
                print 'a: ',a
                print 'b: ',b
                print '-'*20
        print max(len(a),len(b))

lengthOfLongestSubstring("abcabcbb")