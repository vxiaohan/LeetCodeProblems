import unittest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        if row < 1:
            return 0
        column = len(obstacleGrid[0])
        if column < 1:
            return 0
        dp = [[0 for j in range(column)] for i in range(row)]

        blocked = False
        for j in range(column):
            if obstacleGrid[0][j] == 1:
                blocked = True
            dp[0][j] = 1 if not blocked else 0

        blocked = False
        for i in range(row):
            if obstacleGrid[i][0] == 1:
                blocked = True
            dp[i][0] = 1 if not blocked else 0
        for i in range(1, row):
            for j in range(1, column):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

class TestUniquePath(unittest.TestCase):
    def testUniquePathWithObstacles(self):
        test = Solution()
        self.assertEqual(test.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]), 2)
        self.assertEqual(test.uniquePathsWithObstacles([
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]), 1)
        self.assertEqual(test.uniquePathsWithObstacles([
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]), 0)
        self.assertEqual(test.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]
        ]), 3)


if __name__ == '__main__':
    unittest.main()
