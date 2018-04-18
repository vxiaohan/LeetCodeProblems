import unittest


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line_1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        line_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        line_3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        alphabet = [line_1, line_2, line_3]
        result_list = []
        for word in words:
            one_line = True
            line_of_first_letter = 0
            for line_of_first_letter in range(0, 3):
                if word[0] in alphabet[line_of_first_letter]:
                    break
            for i in range(1, len(word)):
                if word[i] not in alphabet[line_of_first_letter]:
                    one_line = False
                    break
            if one_line:
                result_list.append(word)
        return result_list

class TestFindWords(unittest.TestCase):
    def testFindWords(self):
        test = Solution()
        self.assertListEqual(test.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])
