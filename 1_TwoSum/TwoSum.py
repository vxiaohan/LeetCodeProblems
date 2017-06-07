import unittest

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        nums_size = len(sorted_nums)
        for i in range(0,nums_size-1):
            if sorted_nums[i] > target/2:
                break
            for j in range(i+1,nums_size):
                temp_sum = sorted_nums[i] + sorted_nums[j]
                if temp_sum == target:
                    first_index = nums.index(sorted_nums[i])
                    last_index = nums.index(sorted_nums[j])
                    if first_index < last_index:
                        return [first_index, last_index]
                    elif first_index == last_index:
                        last_index = nums.index(sorted_nums[j],first_index+1)
                        return [first_index,last_index]
                    else:
                        return [last_index, first_index]
                elif temp_sum > target:
                    break
        return []



class TwoSumTestCase(unittest.TestCase):
    def test_sum(self):
        test_two_sum = Solution()
        self.assertEqual(test_two_sum.twoSum([2, 7, 11, 15],9), [0,1])
        self.assertEqual(test_two_sum.twoSum([3,3],6),[0,1])

if __name__ == '__main__':
    unittest.main()