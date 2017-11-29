import unittest


class Solution:
    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k_max = int(len(prices) / 2)
        k = min(k, k_max)
        max_profit = [[0] * len(prices)] * k
        if k_max < 1:
            return 0
        for i in range(0, k):
            if i == 0:
                min_price = prices[0]
                current_max_profit = 0
                for j in range(1, len(prices)):
                    if prices[j] < min_price:
                        min_price = prices[j]
                    else:
                        current_max_profit = max(current_max_profit, prices[j] - min_price)
                        max_profit[i][j] = current_max_profit
            else:
                max_price = prices[-1]
                current_max_profit = 0
                for j in range(len(prices)-1, i*k-1 , -1):
                    for j in range(1, len(prices)):
                        if prices[j] > max_price:
                            max_price = prices[j]
                        else:
                            current_max_profit = max(current_max_profit, prices[j] - min_price)
                            max_profit[i][j] = current_max_profit
        return 0


class MaxRorofitTestCase(unittest.TestCase):
    def testMaxProfit(self):
        test = Solution()
        self.assertEqual(test.maxProfit(2,[1, 2, 3, 1, 2, 4, 1, 5]), 6)


if __name__ == '__main__':
    unittest.main()
