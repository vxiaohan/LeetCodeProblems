import unittest


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        max_index = m + n - 1
        nums1_index = m - 1
        nums2_index = n - 1
        for i in range(max_index, -1, -1):
            if nums2_index < 0:
                return
            if nums1_index < 0:
                nums1[i] = nums2[nums2_index]
                nums2_index -= 1
            else:
                if nums1[nums1_index] > nums2[nums2_index]:
                    nums1[i] = nums1[nums1_index]
                    nums1_index -= 1
                else:
                    nums1[i] = nums2[nums2_index]
                    nums2_index -= 1


class TestMerge(unittest.TestCase):
    def testMerge(self):
        test = Solution()
        for i in range(10000):
            num1 = [1, 4, 5, 0, 0, 0, 0]
            num2 = [1, 2, 3, 8]
            test.merge(num1, 3, num2, len(num2))
            self.assertEqual(num1, [1, 1, 2, 3, 4, 5, 8])


if __name__ == '__main__':
    unittest.main()
