import unittest

'''
Work but timeout
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        dp = [[10000 for i in range(n + 1)] for j in range(n + 1)]
        for j in range(n + 1):
            dp[1][j] = j - 1
        for j in range(2, n + 1):
            for i in range(2, j):
                if dp[i][j - i] < 10000:
                    dp[i][j] = dp[i][j - i] + 1
            min_value = 10000
            for k in range(0, j + 1):
                if dp[k][j] < min_value:
                    min_value = dp[k][j]
            dp[j][j] = min_value + 1
        #for i in range(n+1):
        #    print(dp[i])
        return dp[-1][-1]
'''


class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        dp = [10000 for i in range(n + 1)]
        dp[0] = dp[1] = 0
        for j in range(2, n + 1):
            for i in range(1, j):
                if j % i == 0:
                    dp[j] = dp[j] if dp[j] < dp[i] + j / i else dp[i] + j / i
        return int(dp[-1])


class TestMinSteps(unittest.TestCase):
    def testMinSteps(self):
        test = Solution()
        # self.assertEqual(test.minSteps(3), 3)
        #self.assertEqual(test.minSteps(4), 4)
        # self.assertEqual(test.minSteps(6), 5)
        self.assertEqual(test.minSteps(908), 231)


if __name__ == '__main__':
    unittest.main()
