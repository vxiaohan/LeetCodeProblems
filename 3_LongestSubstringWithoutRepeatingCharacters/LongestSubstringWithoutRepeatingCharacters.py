import unittest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringList = list(s)
        stringLength = len(stringList)
        if stringLength == 0:
            return 0
        maxLength = 0
        headIndex = 0
        while headIndex + maxLength + 1 <= stringLength:
            subList = stringList[headIndex:headIndex+maxLength+1]
            subDic = set(subList)
            if len(subDic) == len(subList):
                maxLength += 1
            else:
                headIndex += 1
        return maxLength

class LongestSubstringTestCase(unittest.TestCase):
    def test_longest(self):
        test = Solution()
        self.assertEqual(test.lengthOfLongestSubstring('b'),1)
        self.assertEqual(test.lengthOfLongestSubstring('ab'), 2)
        self.assertEqual(test.lengthOfLongestSubstring('aaaabbbbb'), 2)

if __name__ == '__main__':
    unittest.main()
