__author__ = 'lyb-mac'
def compareVersion( version1, version2):
        v1 = map(int,version1.split("."))

        v2 = map(int,version2.split("."))
        if len(v1) < len(v2):
            v1.extend([0]*(len(v2)-len(v1)))
        else:
            v2.extend([0]*(len(v1)-len(v2)))
        print v1,v2
        return cmp(v1,v2)

compareVersion('01','1')