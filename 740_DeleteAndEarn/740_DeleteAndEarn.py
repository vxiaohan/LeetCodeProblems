import unittest


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        index_list = list(set(nums))
        sum_list = [0] * len(index_list)
        curr_index = 0
        pre_value = index_list[0]
        for i in range(len(nums)):
            if nums[i] == pre_value:
                sum_list[curr_index] += pre_value
            else:
                curr_index += 1
                pre_value = nums[i]
                sum_list[curr_index] += pre_value
        dp_delete = [0] * len(index_list)
        dp_hold = [0] * len(index_list)
        dp_delete[0] = sum_list[0]
        dp_deleted_by_pre = [0] * len(index_list)
        for i in range(1, len(index_list)):
            pre_continue = True if index_list[i] - 1 == index_list[i - 1] else False
            # dp_delete
            if pre_continue:
                dp_delete[i] = max([dp_hold[i - 1], dp_deleted_by_pre[i - 1]]) + sum_list[i]
            else:
                dp_delete[i] = max([dp_hold[i - 1], dp_deleted_by_pre[i - 1], dp_delete[i - 1]]) + sum_list[i]

            # dp_hold
            if pre_continue:
                dp_hold[i] = max(dp_hold[i - 1], dp_deleted_by_pre[i - 1])
            else:
                dp_hold[i] = max([dp_hold[i - 1], dp_deleted_by_pre[i - 1], dp_delete[i - 1]])

            # dp_deleted_by_pre
            if pre_continue:
                dp_deleted_by_pre[i] = dp_delete[i - 1]
            else:
                dp_deleted_by_pre[i] = 0
        return max([dp_deleted_by_pre[-1], dp_delete[-1], dp_hold[-1]])


class TestDelete(unittest.TestCase):
    def testDeleteAndEarn(self):
        test = Solution()
        self.assertEqual(test.deleteAndEarn([3, 4, 2]), 6)
        self.assertEqual(test.deleteAndEarn([2, 2, 3, 3, 3, 4]), 9)
        self.assertEqual(test.deleteAndEarn([3, 1]), 4)
        self.assertEqual(test.deleteAndEarn([1, 1, 1, 2, 4, 5, 5, 5, 6]), 18)


if __name__ == '__main__':
    unittest.main()
