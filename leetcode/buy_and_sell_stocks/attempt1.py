class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                if prices[sell] - prices[buy] > maxProfit:
                    maxProfit = prices[sell] - prices[buy]

            sell += 1

        return maxProfit