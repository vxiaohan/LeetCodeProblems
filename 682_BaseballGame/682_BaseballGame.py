import unittest


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = [0] * len(ops)
        points_index = 0
        for a in ops:
            if a == "+":
                points[points_index] = points[points_index - 2] + points[points_index - 1]
                points_index += 1
            elif a == "D":
                points[points_index] = points[points_index - 1] * 2
                points_index += 1
            elif a == "C":
                points_index -= 1
            else:
                points[points_index] = int(a)
                points_index += 1
        if points_index == 0:
            return 0
        else:
            return sum(points[:points_index])


class TestCalPoints(unittest.TestCase):
    def testCalPoints(self):
        test = Solution()
        self.assertEqual(test.calPoints(["5", "2", "C", "D", "+"]), 30)
        self.assertEqual(test.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)


if __name__ == '__main__':
    unittest.main()
