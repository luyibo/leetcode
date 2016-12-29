class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [True]*n
        res[0] = res[1] = False
        cnt = n-2
        sq = int(round(n**0.5))
        for i in xrange(2,sq+1):
                if res[i]:
                    res[i * i: n: i] = [False] * len(xrange(i * i, n, i))
        return cnt

s = Solution()
s.countPrimes(20)