class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # iterate right, never really look left since you can't transact back in time
        max_profit = 0
        for i in range(len(prices)):
            sell_prices = prices[i+1:]
        
            if sell_prices:
                if (max(sell_prices) - prices[i]) > max_profit:
                    max_profit = max(sell_prices) - prices[i]
                    print(max_profit)
        return max_profit
