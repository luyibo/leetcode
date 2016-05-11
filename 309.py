__author__ = 'lyb-mac'
import operator
def maxProfit( prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        temp = 0
        prices.reverse()
        i = 0
        while i < len(prices)-1:
            sum = prices[i]-prices[i+1]
            if sum>0:
                temp = sum + temp
                i = i + 1
            
        return temp


print maxProfit([4,1,2,5])