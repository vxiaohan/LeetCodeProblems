import unittest


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column_len = len(grid[0])
        row_len = len(grid)
        sum_value = [[0 for i in range(column_len)] for j in range(row_len)]
        for i in range(row_len):
            for j in range(column_len):
                if i == 0 and j == 0:
                    sum_value[i][j] = grid[0][0]
                elif i == 0:
                    sum_value[i][j] = sum_value[i][j - 1] + grid[i][j]
                elif j == 0:
                    sum_value[i][j] = sum_value[i - 1][j] + grid[i][j]
                else:
                    sum_value[i][j] = min([sum_value[i - 1][j], sum_value[i][j - 1]]) + grid[i][j]
        return sum_value[-1][-1]


class MinPathSumTestCase(unittest.TestCase):
    def testMinPathSum(self):
        test = Solution()
        self.assertEqual(test.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(test.minPathSum([[1,2,5],[3,2,1]]),6)


if __name__ == '__main__':
    unittest.main()
