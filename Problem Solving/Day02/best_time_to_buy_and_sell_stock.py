# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

# Solution One

# Submission Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1807482338/
def maxProfit(prices: List[int]) -> int:
        max_profit = float('-inf')
        profit = 0
        while(len(prices)):
            min_value = min(prices)
            min_index = prices.index(min_value)
            right_side = prices[min_index+1:]
            max_right = max(right_side) if len(right_side) else -1
            if max_right != -1 and max_right > min_value:
                profit = max_right - min_value
            
            if (max_profit < profit):
                max_profit = profit
                
            prices = prices[:min_index]
        
        return max_profit
    
# Solution Two - Optimal Approach
# Submission Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1807417546/
def maxProfit(self, prices: List[int]) -> int:
        minimum_price = 99999999
        profit = 0
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            elif price - minimum_price > profit:
                profit = price - minimum_price

        return profit