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
        holdProfit = [0] * len(prices)
        unholdProfit = [0] * len(prices)
        buyProfit = [0] * len(prices)
        sellProfit = [0] *len(prices)
        holdProfit[0] = -2
        buyProfit[0] = -2
        for i in range(1, len(prices)):
            holdProfit[i] = max([holdProfit[i - 1] + (prices[i] - prices[i - 1]), unholdProfit[i - 1] - fee])
            unholdProfit[i] = max(unholdProfit[i-1], holdProfit[i-1])
        holdProfit[-1] -= fee
        print(holdProfit)
        print(unholdProfit)
        return max([holdProfit[-1], unholdProfit[-1]])


class BestTimeTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit([1, 3, 2, 8, 4, 9], 2), 8)
        self.assertEqual(test.maxProfit([1, 5, 9], 2), 6)


if __name__ == '__main__':
    unittest.main()
