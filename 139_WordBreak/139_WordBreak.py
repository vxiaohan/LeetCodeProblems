import unittest


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dict_words = {}
        max_length = 0
        for word in wordDict:
            dict_words[word] = 1
            max_length = max([max_length, len(word)])
        break_list = []
        for current_index in range(len(s)):
            if len(break_list) == 0:
                if s[0: current_index + 1] in wordDict:
                    break_list.append(current_index)
                else:
                    continue
            else:
                for j in range(len(break_list)):
                    index = len(break_list) - j - 1
                    if current_index - break_list[index] > max_length:
                        break
                    else:
                        if s[break_list[index] + 1: current_index + 1] in wordDict:
                            break_list.append(current_index)
                            break
                if break_list[-1] != current_index:
                    if s[0: current_index + 1] in wordDict:
                        break_list.append(current_index)
        if len(break_list) == 0:
            return False
        if break_list[-1] == len(s) - 1:
            return True
        else:
            return False


class WordBreakTestCase(unittest.TestCase):
    def testWordBreak(self):
        test = Solution()
        self.assertEqual(test.wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(test.wordBreak("leetode", ["leet", "code"]), False)
        self.assertEqual(test.wordBreak("leetcode", ["leet", "cod", "de", "co"]), True)
        self.assertEqual(test.wordBreak("leetcode", ["eet", "cod", "de", "co"]), False)
        self.assertEqual(test.wordBreak("goalspecial", ["go", "goal", "goals", "special"]), True)


if __name__ == '__main__':
    unittest.main()
