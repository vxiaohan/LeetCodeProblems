import unittest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2
        k_max = int(len(prices) / 2)
        k = min(k, k_max)
        max_profit = [[0] * len(prices)] * 2
        if k_max < 1:
            return 0
        buy1 = [0] * len(prices)
        buy2 = [0] * len(prices)
        buy1[0] = -prices[0]
        buy2[0] = float('-inf')
        sell1 = [0] * len(prices)
        sell2 = [0] * len(prices)
        for i in range(1, len(prices)):
            buy1[i] = max([buy1[i - 1], -prices[i]])
            sell1[i] = max([sell1[i - 1], buy1[i - 1] + prices[i]])
            buy2[i] = max([buy2[i - 1], sell1[i - 1] - prices[i]])
            sell2[i] = max([sell2[i - 1], buy2[i - 1] + prices[i]])
        return max(sell1[-1], sell2[-1])

class MaxRorofitTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit([1, 2, 3, 1, 2, 4, 1, 5]), 7)
        self.assertEqual(test.maxProfit([1,2]),1)

if __name__ == '__main__':
    unittest.main()
