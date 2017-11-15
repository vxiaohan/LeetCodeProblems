import unittest


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n <= 0:
            return 0
        v_k_1 = 2
        v_k_2 = 1
        v = 0
        for i in range(3, n+1):
            v = v_k_1 + v_k_2
            v_k_2 = v_k_1
            v_k_1 = v
        return v


class ClimbingStairsTestCase(unittest.TestCase):
    def testClimbStairs(self):
        test = Solution()
        self.assertEqual(test.climbStairs(2), 2)
        self.assertEqual(test.climbStairs(3), 3)
        self.assertEqual(test.climbStairs(4), 5)


if __name__ == "__main__":
    unittest.main()
