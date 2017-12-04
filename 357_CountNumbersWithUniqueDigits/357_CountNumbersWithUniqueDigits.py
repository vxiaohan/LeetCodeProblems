import unittest
import math


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = 10
        factorial_10 = math.factorial(10)
        factorial_9 = math.factorial(9)
        factorial_cache = [0] * 10
        for i in range(2, n + 1):
            if factorial_cache[10 - i] == 0:
                factorial_cache[10 - i] = math.factorial(10 - i)
            if factorial_cache[9 - i + 1] == 0:
                factorial_cache[9 - i + 1] = math.factorial(9 - (i - 1))
            dp = dp + int(factorial_10 / factorial_cache[10 - i]) - int(factorial_9 / factorial_cache[9 - i + 1])
        return dp


class TestNumbersWithUniqueDigits(unittest.TestCase):
    def testCountNumberWithUniqueDigits(self):
        test = Solution()
        self.assertEqual(test.countNumbersWithUniqueDigits(2), 91)
        self.assertEqual(test.countNumbersWithUniqueDigits(3), 739)


if __name__ == '__main__':
    unittest.main()
