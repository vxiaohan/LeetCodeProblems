import unittest


class Solution:
    def dfs(self, numbers, target, ):

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        sorted_num = sorted(nums, reverse=True)
        if k > length:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target_sum = total / k
        if sorted_num[0] > target_sum:
            return False
        return False


class PartitionKTestCase(unittest.TestCase):
    def testCanPartitionKSubsets(self):
        test = Solution()
        self.assertEqual(test.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4), True)
        self.assertEqual(test.canPartitionKSubsets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1), True)


if __name__ == '__main__':
    unittest.main()
