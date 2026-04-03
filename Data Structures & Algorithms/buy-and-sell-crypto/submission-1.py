class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 

        buy_day = 0
        total_days = len(prices)

        for sell_day in range(buy_day, total_days): 

            if prices[buy_day] > prices[sell_day]: 
                buy_day = sell_day

            else: 

                max_profit = max(max_profit, prices[sell_day] - prices[buy_day])

        return max_profit
        
        