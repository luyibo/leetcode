__author__ = 'user'
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.combination(k,n,[],1)
        return self.result

    def combination(self,k,n,current,start):
        if n==0 and k==0:
            return self.result.append(current)
        for i in range(start,10):
            if start>n:break
            self.combination(k-1,n-i,current+[i],i+1)
s = Solution()
print s.combinationSum3(3,7)