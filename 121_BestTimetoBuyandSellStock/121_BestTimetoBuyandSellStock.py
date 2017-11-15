import unittest


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) > 0:
            curr_min_price = prices[0]
        else:
            return 0
        curr_max_profit = 0
        for number in prices:
            if number < curr_min_price:
                curr_min_price = number
            else:
                curr_profit = number - curr_min_price
                if curr_profit > curr_max_profit:
                    curr_max_profit = curr_profit
        return curr_max_profit


class BestTimeTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(test.maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
