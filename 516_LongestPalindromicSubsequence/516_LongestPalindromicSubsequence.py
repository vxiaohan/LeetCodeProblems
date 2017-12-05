import unittest

'''
# Timeout
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(1, len(s)):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = dp[i][j - 1] if dp[i][j - 1] > dp[i + 1][j] else dp[i + 1][j]
        return dp[0][-1]
'''



class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        dp = [[0, 0] for i in range(length)]
        dp[0][0] = 1
        for j in range(1, length):
            index_j = j % 2
            dp[j][index_j] = 1
            index_j_1 = 0 if index_j == 1 else 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][index_j] = dp[i + 1][index_j_1] + 2
                else:
                    dp[i][index_j] = dp[i][index_j_1] if dp[i][index_j_1] > dp[i + 1][index_j] else dp[i + 1][index_j]
        return dp[0][(length - 1) % 2]


class TestLongest(unittest.TestCase):
    def testLongestPalindromeSubseq(self):
        test = Solution()
        self.assertEqual(test.longestPalindromeSubseq("bbab"), 3)
        self.assertEqual(test.longestPalindromeSubseq("betahifadb"), 5)
        self.assertEqual(test.longestPalindromeSubseq("cbbd"), 2)
        self.assertEqual(test.longestPalindromeSubseq("aba"), 3)
        self.assertEqual(test.longestPalindromeSubseq(
            "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"),
            494)


if __name__ == '__main__':
    unittest.main()
