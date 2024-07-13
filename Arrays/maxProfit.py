class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        best_selling_price = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if output < best_selling_price - prices[i]:
                output = best_selling_price - prices[i]
            if best_selling_price < prices[i]:
                best_selling_price = prices[i]
        return output
