import unittest


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_length = len(s)
        if s_length == 0:
            return True
        if len(t) == 0 or s_length > len(t):
            return False
        s_index = 0
        for j in range(0,len(t)):
            if t[j] == s[s_index]:
                s_index += 1
            if s_index == s_length:
                return True
        return False

class TestSubsequence(unittest.TestCase):
    def testIsSubsequence(self):
        test = Solution()
        self.assertEqual(test.isSubsequence("abc", "ahbgdc"), True)
        self.assertEqual(test.isSubsequence("axc", "ahbgdc"), False)


if __name__ == '__main__':
    unittest.main()
