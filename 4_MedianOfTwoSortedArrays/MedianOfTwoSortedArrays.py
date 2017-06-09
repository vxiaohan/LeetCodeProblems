import math
import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        index_1 = -1
        index_2 = -1
        total_length = length1 + length2
        is_length_odd = True if (int(total_length % 2) == 0) else False
        k_total = int(total_length / 2 - 1) if is_length_odd else int((total_length - 1) / 2)
        rest = k_total
        if length1 == 0 and length2 == 0:
            return []
        elif length1 == 0:
            if is_length_odd:
                return float(nums2[int(total_length / 2 - 1)] + nums2[int(total_length / 2)]) / 2
            else:
                return nums2[int((total_length - 1) / 2)]
        elif length2 == 0:
            if is_length_odd:
                return float(nums1[int(total_length / 2 - 1)] + nums1[int(total_length / 2)]) / 2
            else:
                return nums1[int((total_length - 1) / 2)]
        while rest > 0:
            k = 1 if rest == 1 else int(math.floor(rest / 2))
            if index_1 == length1:
                index_2 += rest
                break
            if index_2 == length2:
                index_1 += rest
                break
            temp_index1 = min([index_1 + k, length1 - 1])
            temp_index2 = min([index_2 + k, length2 - 1])
            if nums1[temp_index1] <= nums2[temp_index2]:
                rest -= temp_index1 - index_1
                if temp_index1 == length1 - 1:
                    index_1 = length1
                else:
                    index_1 = temp_index1
            else:
                rest -= temp_index2 - index_2
                if temp_index2 == length2 - 1:
                    index_2 = length2
                else:
                    index_2 = temp_index2
        if is_length_odd:
            calculate_list = nums1[index_1 + 1:min([length1, index_1 + 3])]
            calculate_list += nums2[index_2 + 1:min([length2, index_2 + 3])]
            list.sort(calculate_list)
            return float(calculate_list[0] + calculate_list[1]) / 2
        else:
            if index_1 == length1:
                return nums2[index_2 + 1]
            elif index_2 == length2:
                return nums1[index_1 + 1]
            else:
                return min([nums1[min(index_1 + 1, length1 - 1)], nums2[min(index_2 + 1, length2 - 1)]])


class FindMedianTestCase(unittest.TestCase):
    def test_median(self):
        test = Solution()
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3], [4, 5]), 3)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 4, 5], [0]), 2.5)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 6, 8], [4]), 3.5)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 6, 8], [4, 5]), 4)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 4], []), 2.5)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3], []), 2)
        self.assertEqual(test.findMedianSortedArrays([], []), [])
        self.assertEqual(test.findMedianSortedArrays([2, 2, 2], [2, 2, 2, 2]), 2)
        self.assertEqual(test.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(test.findMedianSortedArrays([1], [2, 3]), 2)


if __name__ == '__main__':
    unittest.main()
