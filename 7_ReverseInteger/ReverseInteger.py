import unittest


class Solution:
    def reverse(self, x:int) -> int:
        negative = False
        x_str = ""
        if x < 0:
            negative = True
        if x % 10 == 0:
            if negative:
                x_str = "-" + str(int(-x/10))[::-1]
            else:
                x_str = str(int(x/10))[::-1]
        else:
            if negative:
                x_str = "-" + str(-x)[::-1]
            else:
                x_str = str(x)[::-1]
        reverse_int = int(x_str)
        if reverse_int < -2147483648 or reverse_int > 2147483647:
            return 0
        return reverse_int

class ReverseIntegerTestCase(unittest.TestCase):
    def testReverseInteger(self):
        test = Solution()
        self.assertEqual(test.reverse(123), 321)
        self.assertEqual(test.reverse(-123), -321)
        self.assertEqual(test.reverse(120), 21)
        self.assertEqual(test.reverse(-120), -21)
        self.assertEqual(test.reverse(1534236469), 0)
if __name__ == '__main__':
    unittest.main()