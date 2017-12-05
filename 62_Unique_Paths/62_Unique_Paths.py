import unittest


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            for i in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class UniquePathTest(unittest.TestCase):
    def testUniquePaths(self):
        test = Solution()
        self.assertEqual(test.uniquePaths(1, 2), 1)
        self.assertEqual(test.uniquePaths(100, 100), 22750883079422934966181954039568885395604168260154104734000)


if __name__ == '__main__':
    unittest.main()
