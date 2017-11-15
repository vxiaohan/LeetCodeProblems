import unittest


class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for column in range(len(B))] for row in range(len(A))]
        max_length = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
        return max_length


class MaxLengthSubArrayTestCase(unittest.TestCase):
    def testFindLength(self):
        test = Solution()
        self.assertEqual(test.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]), 3)


if __name__ == '__main__':
    unittest.main()
