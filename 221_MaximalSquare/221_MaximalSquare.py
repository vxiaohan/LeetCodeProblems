import unittest


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1:
            return 0

        row = len(matrix)
        column = len(matrix[0])
        if column < 1:
            return 0
        max_dp = 0
        dp = [[[0, 0, 0, 0] for j in range(column)] for i in range(row)]
        continue_count = 0
        for i in range(row):
            if matrix[i][0] == '1':
                continue_count += 1
                dp[i][0][0] = 1
                dp[i][0][1] = continue_count
                dp[i][0][2] = 1
                dp[i][0][3] = continue_count
                max_dp = 1
            else:
                continue_count = 0

        continue_count = 0
        for j in range(column):
            if matrix[0][j] == '1':
                continue_count += 1
                dp[0][j][0] = continue_count
                dp[0][j][1] = 1
                dp[0][j][2] = continue_count
                dp[0][j][3] = 1
                max_dp = 1
            else:
                continue_count = 0

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == '1':
                    dp[i][j][2] = dp[i][j - 1][2] + 1
                    dp[i][j][3] = dp[i - 1][j][3] + 1
                    dp[i][j][0] = min([dp[i][j][2], dp[i - 1][j - 1][0] + 1])
                    dp[i][j][1] = min(dp[i][j][3], dp[i - 1][j - 1][1] + 1)
                    min_dp = min(dp[i][j][0], dp[i][j][1])
                    if min_dp > max_dp:
                        max_dp = min_dp
        return max_dp * max_dp


class TestMaximalSquare(unittest.TestCase):
    def testMaximalSquare(self):
        test = Solution()

        self.assertEqual(
            test.maximalSquare([["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
                                ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
                                ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
                                ["1", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0"],
                                ["1", "0", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1"],
                                ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1"],
                                ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                                ["1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1"]]), 25)

        self.assertEqual(test.maximalSquare([["0", "0", "0", "1"],
                                             ["1", "1", "0", "1"],
                                             ["1", "1", "1", "1"],
                                             ["0", "1", "1", "1"],
                                             ["0", "1", "1", "1"]]), 9)
        self.assertEqual(test.maximalSquare([["1", "0", "1", "0", "0"],
                                             ["1", "0", "1", "1", "1"],
                                             ["1", "1", "1", "1", "1"],
                                             ["1", "0", "0", "1", "0"]]), 4)


if __name__ == '__main__':
    unittest.main()
