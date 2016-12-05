__author__ = 'user'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stock = []
        total = 0
        for i in range(1,len(prices)):
            stock.append(prices[i]-prices[i-1])
        for price in stock:
            if price>0:
                total += price
        return total

s = Solution()
print s.maxProfit([5,3,7,2,9,6])