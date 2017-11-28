import unittest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        holdProfit = [0] * len(prices)
        unholdProfit = [0] * len(prices)
        for i in range(1, len(prices)):
            holdProfit[i] = max([holdProfit[i - 1] + (prices[i] - prices[i - 1]), unholdProfit[i - 1]])
            unholdProfit[i] = max([holdProfit[i - 1], unholdProfit[i - 1]])
        return max([holdProfit[-1], unholdProfit[-1]])

class BestTimeTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit([1, 2, 3, 0, 2]), 3)


if __name__ == '__main__':
    unittest.main()
