import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_str = list(str(x))
        length = len(num_str)
        if length == 1:
            return True
        elif length % 2 == 0:
            num_str_head = num_str[:int(length/2)]
            num_str_end = num_str[:int(length/2)-1:-1]
        else:
            num_str_head = num_str[:int((length-1)/2)]
            num_str_end = num_str[:int((length-1)/2):-1]
        if num_str_head == num_str_end:
            return True
        return False


class IsPalindromeTestCase(unittest.TestCase):
    def testIsPalindrome(self):
        test = Solution()
        self.assertEqual(test.isPalindrome(121), True)
        self.assertEqual(test.isPalindrome(-121), False)
        self.assertEqual(test.isPalindrome(10), False)
        self.assertEqual(test.isPalindrome(123456789987654321), True)


if __name__ == "__main__":
    unittest.main()
