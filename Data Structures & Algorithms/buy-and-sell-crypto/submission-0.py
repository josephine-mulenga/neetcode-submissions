class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        n = len(prices)

        for i in range(1,n):
            if prices[i] < prices[left]:
                left = i
            else:
                profit = prices[i] - prices[left]
                max_profit = max(max_profit, profit)
        return max_profit

            

        