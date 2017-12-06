import unittest


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return len(s)
        dp = [0] * len(s)
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1

        if len(s) == 1:
            return 1

        if int(s[:2]) <= 26 and s[1] != '0':
            dp[1] = 2
        elif int(s[:2]) > 26 and s[1] == '0':
            return 0
        else:
            dp[1] = 1
        for i in range(2, len(s)):
            if s[i] == '0':
                if 2 >= int(s[i - 1]) > 0:
                    dp[i] = min(dp[i - 1], dp[i - 2])
                else:
                    return 0
            else:
                if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]


class TestDecodings(unittest.TestCase):
    def testNumDecodings(self):
        test = Solution()
        self.assertEqual(test.numDecodings("1212"), 5)
        self.assertEqual(test.numDecodings("611"), 2)
        self.assertEqual(test.numDecodings("227"), 2)
        self.assertEqual(test.numDecodings('101'), 1)
        self.assertEqual(test.numDecodings('12'), 2)
        self.assertEqual(test.numDecodings('123'), 3)
        self.assertEqual(test.numDecodings("301"), 0)
        self.assertEqual(test.numDecodings('10'), 1)
        self.assertEqual(test.numDecodings('100'), 0)


if __name__ == '__main__':
    unittest.main()
