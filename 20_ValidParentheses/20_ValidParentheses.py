import unittest
import queue


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [''] * len(s)
        stack_size = 0
        for a in s:
            if stack_size == 0:
                stack[0] = a
                stack_size += 1
            else:
                pre = stack[stack_size - 1]
                if (pre == '[' and a == ']') or (pre == '(' and a == ')') or (pre == '{' and a == '}'):
                    stack_size -= 1
                else:
                    stack[stack_size] = a
                    stack_size += 1

        if stack_size == 0:
            return True
        else:
            return False


class TestIsValid(unittest.TestCase):
    def testIsValid(self):
        test = Solution()
        self.assertEqual(test.isValid('[]{{()}}'), True)
        self.assertEqual(test.isValid('['), False)


if __name__ == '__main__':
    unittest.main()
