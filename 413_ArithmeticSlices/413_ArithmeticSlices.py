import unittest


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        length = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                if length[i - 1] == 0:
                    length[i] = 3
                else:
                    length[i] = length[i - 1] + 1
        last_zero = -1
        length_list = []
        for i in range(len(length)):
            if length[i] == 0:
                if last_zero != i - 1:
                    length_list.append(length[i - 1])
                last_zero = i
        if length[-1] != 0:
            length_list.append(length[-1])
        total = 0
        for n in length_list:
            total += int((n - 1) * (n - 2) / 2)
        return total


class ArithmeticSlicesTestCase(unittest.TestCase):
    def testNumberOfArithmeticSlices(self):
        test = Solution()
        self.assertEqual(test.numberOfArithmeticSlices([1, 2, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
