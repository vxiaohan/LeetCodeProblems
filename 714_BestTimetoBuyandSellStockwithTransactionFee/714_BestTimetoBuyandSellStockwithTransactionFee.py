import unittest


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        sellProfit = [0] * len(prices)
        holdProfit = [0] * len(prices)
        holdProfit[0] = - prices[0]
        for i in range(1, len(prices)):
            sellProfit[i] = max([sellProfit[i - 1], holdProfit[i - 1] + prices[i] - fee])
            holdProfit[i] = max([holdProfit[i - 1], sellProfit[i - 1] - prices[i]])
        return sellProfit[-1]


class BestTimeTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit([1, 3, 2, 8, 4, 9], 2), 8)
        self.assertEqual(test.maxProfit([1, 5, 9], 2), 6)
        self.assertEqual(test.maxProfit([1, 3, 7, 5, 10, 3], 3), 6)
        self.assertEqual(test.maxProfit([1, 4, 6, 2, 8, 3, 10, 14], 3), 13)


if __name__ == '__main__':
    unittest.main()
