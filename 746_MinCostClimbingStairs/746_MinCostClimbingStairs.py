import unittest


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0
        dp_0 = 0
        dp_1 = cost[0]
        for k in range(2, len(cost) + 1):
            if k % 2 == 0:
                dp_0 = min(dp_0, dp_1) + cost[k - 1]
            else:
                dp_1 = min(dp_0, dp_1) + cost[k - 1]
        return min(dp_0, dp_1)


class TestMinCost(unittest.TestCase):
    def testMinCost(self):
        test = Solution()
        for i in range(10000):
            self.assertEqual(test.minCostClimbingStairs([0, 0, 1, 1]), 1)
            self.assertEqual(test.minCostClimbingStairs([10, 15, 20]), 15)
            self.assertEqual(test.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)


if __name__ == '__main__':
    unittest.main()
