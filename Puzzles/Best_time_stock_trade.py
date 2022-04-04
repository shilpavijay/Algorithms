'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

import time
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = time.time()
        buy_val = prices[0]
        max_profit = 0
        for val in prices[1:]:
            profit = val - buy_val
            if profit > max_profit:
                max_profit = profit
            if val < buy_val:
                buy_val = val
        time_taken = time.time() - start
        print(time_taken)
        return max_profit
        
s = Solution()
prices = [7,3,2,1]
print(s.maxProfit(prices))        
        
#Alternate solution        
# class Solution(object):
    # def maxProfit(self, prices):
    # """
    # :type prices: List[int]
    # :rtype: int
    # """
        # start = time.time()
        # max_profit = 0
        # for buy_idx,buy_val in enumerate(prices):
        #     if buy_idx < len(prices)-1:
        #         profit = max(prices[buy_idx+1:]) - buy_val
        #         # profit = sorted(prices[buy_idx+1:])[-1] - buy_val
        #         if profit > max_profit:
        #             max_profit = profit
        # time_taken = time.time() - start
        # print(time_taken)
        # return max_profit