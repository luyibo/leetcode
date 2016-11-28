__author__ = 'lyb-mac'
def nthUglyNumber( n):
        """
        :type n: int
        :rtype: int
        """
        l1 = [1]
        i,j,k = 0,0,0
        for l in range(n-1):
            v1,v2,v3 = l1[i]*2,l1[j]*3,l1[k]*5
            m = min(v1,v2,v3)
            if m == v1:
                i+=1
            if m == v2:
                j+=1
            if m == v3:
                k+=1
            l1.append(m)
        return   l1[-1]



print  nthUglyNumber(20)
