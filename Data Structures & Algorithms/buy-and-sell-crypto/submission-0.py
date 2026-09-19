class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(profit, res)
            else:
                left = right

        return res