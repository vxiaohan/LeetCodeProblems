import unittest


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        depth = len(triangle)
        if depth == 0:
            return 0
        if depth == 1:
            return triangle[0][0]

        dp = [[0 for j in range(len(triangle[-1]))] for i in [0, 1]]
        current_index = (len(triangle) - 1) % 2
        for j in range(len(triangle[-1])):
            dp[current_index][j] = triangle[-1][j]
        for i in range(depth - 2, -1, -1):
            previous_index = current_index
            current_index = i % 2
            for j in range(i + 1):
                dp[current_index][j] = min(dp[previous_index][j], dp[previous_index][j+1]) + triangle[i][j]
        return dp[0][0]


class TestMinimumTotal(unittest.TestCase):
    def testMinimumTotal(self):
        test = Solution()
        self.assertEqual(test.minimumTotal([[1], [2, 3]]), 3)
        self.assertEqual(test.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)


if __name__ == '__main__':
    unittest.main()