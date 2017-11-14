import unittest

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_rob_max = 0
        pre_non_rob_max = 0
        for number in nums:
            rob_max = pre_non_rob_max + number
            non_rob_max = max(pre_non_rob_max, pre_rob_max)
            pre_rob_max = rob_max
            pre_non_rob_max = non_rob_max
        return max([pre_rob_max, pre_non_rob_max])



class HouseRobberUnittest(unittest.TestCase):
    def testRob(self):
        pass


if __name__ == "__main__":
    unittest.main()