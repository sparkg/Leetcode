class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        if len(prices) == 2:
            if prices[0] > prices[1]:
                return 0
            else:
                return prices[1] - prices[0]
        max_list = []
        min_list = []
        for i in range(len(prices)):
            if i == 0:
                if prices[i] > prices[i+1]:
                    max_list.append(i)
                if prices[i] < prices[i+1]:
                    min_list.append(i)
            elif (i+1) == len(prices):
                if prices[i] > prices[i-1]:
                    max_list.append(i)
                if prices[i] < prices[i - 1]:
                    min_list.append(i)
            else:
                if prices[i] >= prices[i-1] and prices[i] >= prices[i+1]:
                    if prices[i-1] != prices[i] or prices[i] != prices[i+1]:
                        max_list.append(i)
                if prices[i] <= prices[i - 1] and prices[i] <= prices[i+1]:
                    if prices[i-1] != prices[i] or prices[i] != prices[i+1]:
                        min_list.append(i)
        if len(max_list) == 0 or len(min_list) == 0:
            return 0
        if len(max_list) == 1 and len(min_list) == 1:
            if max_list[0] > min_list[0]:
                return prices[max_list[0]] - prices[min_list[0]]
            else:
                return 0
        price = 0
        counter = -1
        for i in range(len(min_list)):
            if min_list[i] < counter:
                continue
            for j in range(len(max_list)):
                if min_list[i] < max_list[j]:
                    price += (prices[max_list[j]] - prices[min_list[i]])
                    counter = max_list[j]
                    break
        return price

"""
下面是大神的解法
"""
class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans