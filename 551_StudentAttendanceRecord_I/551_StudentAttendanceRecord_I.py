import unittest


class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        absent = 0
        late = 0
        for state in n:
            if state == 'A':
                absent += 1
                late = 0
            elif state == 'L':
                late += 1
            else:
                late = 0
            if absent > 1 or late > 2:
                return False
        return True


class TestRecord(unittest.TestCase):
    def testCheckRecord(self):
        test = Solution()
        self.assertEqual(test.checkRecord("PPALLP"), True)
        self.assertEqual(test.checkRecord("PPALLL"), False)
        self.assertEqual(test.checkRecord("LALL"), True)


if __name__ == '__main__':
    unittest.main()
