import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        list_p = list(p)
        length_p = len(list_p)
        comb_p = 


class TestIsMatch(unittest.TestCase):
    def testMatch(self):
        test = Solution()
        self.assertEqual(test.isMatch("aa", "a"), False)
        self.assertEqual(test.isMatch("aa", "a*"), True)
        self.assertEqual(test.isMatch("ab", ".*"), True)
        self.assertEqual(test.isMatch("aab", "c*a*b"), True)
        self.assertEqual(test.isMatch("mississippi", "mis*is*p*."), True)


if __name__ == "__main__":
    unittest.main()
