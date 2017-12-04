import unittest


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            max_dp = 0
            for j in range(1, i):
                factor = max(dp[j], j)
                if (i - j) * factor > max_dp:
                    max_dp = (i - j) * factor
            dp[i] = max_dp
        return dp[-1]


class IntegerBreakTest(unittest.TestCase):
    def testIntegerBreak(self):
        test = Solution()
        self.assertEqual(test.integerBreak(2), 1)
        self.assertEqual(test.integerBreak(10), 36)


if __name__ == '__main__':
    unittest.main()
