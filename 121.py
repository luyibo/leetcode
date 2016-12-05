__author__ = 'user'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1 or len(prices)==0:return 0
        stocks = []
        for i in range(1,len(prices)):
            stocks.append(prices[i]-prices[i-1])
        nstart = stocks[-1]
        nall = stocks[-1]
        for stock in stocks[-2::-1]:
            if nstart < 0:
                nstart = 0
            nstart += stock
            if nstart > nall:
                nall = nstart
        return max(nall,0)
    def maxProfit2(self,prices):
        Max = 0
        Min = float('inf')
        for price in prices:
            Min = min(Min,price)
            Max = max(Max,price-Min)
        return Max
s = Solution()
print s.maxProfit([1,2])