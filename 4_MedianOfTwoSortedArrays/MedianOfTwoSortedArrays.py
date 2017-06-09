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
        index_1 = 0
        index_2 = 0
        total_length = length1 + length2
        is_length_odd = True if (total_length % 2 == 0) else False
        k_total = int(total_length / 2 - 1) if is_length_odd else int((total_length - 1) / 2)
        rest = k_total
        while rest > 0:
            k = 1 if rest == 1 else int(math.floor(rest / 2))
            if index_1 == length1:
                index_2 += rest
                rest = 0
                break
            if index_2 == length2:
                index_1 += rest
                rest = 0
                break
            temp_index1 = min([index_1 + k, length1 - 1])
            temp_index2 = min([index_2 + k, length2 - 1])
            print((index_1, index_2))
            if nums1[temp_index1] <= nums2[temp_index2]:
                if index_1 == temp_index1 and temp_index1==(length1-1):
                    rest -= temp_index1 - index_1 + 1
                    index_1 = temp_index1 + 1
                else:
                    rest -= temp_index1 - index_1
                    index_1 = temp_index1
            else:
                if index_2 == temp_index2 and temp_index2==(length2-1):
                    rest -= temp_index2 - index_2 + 1
                    index_2 = temp_index2 + 1
                else:
                    rest -= temp_index2 - index_2
                    index_2 = temp_index2
        if is_length_odd:
            calculate_list = nums1[index_1:min([length1, index_1 + 2])]
            calculate_list += nums2[index_2:min([length2, index_2 + 2])]
            list.sort(calculate_list)
            return (calculate_list[0] + calculate_list[1]) / 2
        else:
            if index_1 == length1:
                return nums2[index_2]
            elif index_2 == length2:
                return nums1[index_1]
            else:
                return min([nums1[index_1], nums2[index_2]])


class FindMedianTestCase(unittest.TestCase):
    def test_median(self):
        test = Solution()
        #self.assertEqual(test.findMedianSortedArrays([1, 2, 3], [4, 5]), 3)
        #self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 4, 5], [0]), 2.5)
        #self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 6, 8], [4]), 3.5)
        self.assertEqual(test.findMedianSortedArrays([1, 2, 3, 6, 8], [4,5]), 4)


if __name__ == '__main__':
    unittest.main()
