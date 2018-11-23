class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        if prices[1] >= prices[0]:
            max_price = 1
            min_price = 0
        else:
            max_price = 0
            min_price = 1
        profit = 0
        # 核心思想：当max标号大于min标号时
        # 保留最大的profit
        for i in range(1, len(prices)):
            if prices[i] >= prices[max_price] or (prices[i] > prices[min_price] and min_price > max_price):
                max_price = i
                profit = max(profit, prices[max_price] - prices[min_price])
            elif prices[i] < prices[min_price]:
                min_price = i
        return profit
"""
大神的解法
"""
class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        min_price=prices[0]
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            if price-min_price>max_profit:
                max_profit=price-min_price
        return max_profit