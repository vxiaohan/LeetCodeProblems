import unittest


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        curr_value = 0
        for number in nums:
            curr_value = max([curr_value + number, number, 0])
            if curr_value > max_sum:
                max_sum = curr_value
        if max_sum == 0:
            max_sum = max(nums)
        return max_sum


class MaximumSubArrayTestCase(unittest.TestCase):
    def testMaxSubArray(self):
        test = Solution()
        self.assertEqual(test.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(test.maxSubArray([-1]), -1)

if __name__ == "__main__":
    unittest.main()
