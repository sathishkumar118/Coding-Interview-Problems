class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculate the maximum profit that can be achieved from a single buy and sell of stock.
        
        This function takes a list of integers representing the price of a given stock on different days. 
        It returns the maximum profit that can be made by buying on one of those days and selling on a later day. 
        If no profit can be made, the function returns 0.
        
        Args:
            prices (list[int]): A list of integers representing the stock prices on different days.
        
        Returns:
            int: The maximum profit that can be achieved. If no profit can be made, returns 0.
        
        Example:
            >>> sol = Solution()
            >>> sol.maxProfit([7, 1, 5, 3, 6, 4])
            5
            >>> sol.maxProfit([7, 6, 4, 3, 1])
            0
        
        """
        output = 0
        best_selling_price = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if output < best_selling_price - prices[i]:
                output = best_selling_price - prices[i]
            if best_selling_price < prices[i]:
                best_selling_price = prices[i]
        return output
