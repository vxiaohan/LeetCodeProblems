import unittest


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)


class RangeSumQueryImmutableTestCase(unittest.TestCase):
    def testRangeSum(self):
        test = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(test.sumRange(0, 2), 1)
        self.assertEqual(test.sumRange(2, 5), -1)
        self.assertEqual(test.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
