import unittest


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pre_rob_max_with_first = nums[0]
        pre_non_rob_max_with_first = 0
        pre_rob_max_without_first = 0
        pre_non_rob_max_without_first = 0
        for number in range(1, len(nums) - 1):
            rob_max_with_first = pre_non_rob_max_with_first + nums[number]
            non_rob_max_with_first = max(pre_non_rob_max_with_first, pre_rob_max_with_first)
            rob_max_without_first = pre_non_rob_max_without_first + nums[number]
            non_rob_max_without_first = max(pre_non_rob_max_without_first, pre_rob_max_without_first)
            pre_rob_max_with_first = rob_max_with_first
            pre_non_rob_max_with_first = non_rob_max_with_first
            pre_rob_max_without_first = rob_max_without_first
            pre_non_rob_max_without_first = non_rob_max_without_first

        return max([pre_rob_max_without_first, pre_rob_max_with_first, pre_non_rob_max_with_first,
                    pre_non_rob_max_without_first + nums[-1]])


class TestRobII(unittest.TestCase):
    def testRob(self):
        test = Solution()
        self.assertEqual(test.rob([2, 1, 1, 1]), 3)
        self.assertEqual(test.rob([1, 2, 1, 1]), 3)
        self.assertEqual(test.rob([0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
