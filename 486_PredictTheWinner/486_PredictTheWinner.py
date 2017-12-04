import unittest


class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        if len(nums) == 1:
            return True if nums[0] >= 0 else False
        if len(nums) == 2:
            return True
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
        return True if dp[0][-1] >= 0 else False


class TestPredictTheWinner(unittest.TestCase):
    def testPredictTheWinner(self):
        test = Solution()
        self.assertEqual(test.PredictTheWinner([1, 5, 2]), False)
        self.assertEqual(test.PredictTheWinner([1, 5, 233, 7]), True)


if __name__ == '__main__':
    unittest.main()
