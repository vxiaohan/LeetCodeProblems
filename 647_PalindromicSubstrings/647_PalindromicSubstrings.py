import unittest


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        split_string = ['#' for i in range(len(s) * 2 + 1)]
        split_string[0] = '-'
        split_string[-1] = '+'
        split_string_palin_length = [0 for i in range(len(split_string))]
        split_string_palin_length[0] = 1
        for i in range(len(s)):
            split_string[2 * i + 1] = s[i]
        right_max = 0
        middle = 0
        for i in range(1, len(split_string) - 1):
            if i > right_max:
                middle = i
                length = 1
                while split_string[i - length] == split_string[i + length]:
                    length += 1
                split_string_palin_length[i] = length
                right_max = i + length - 1
            else:
                if split_string_palin_length[middle - (i - middle)] + i <= right_max:
                    length = split_string_palin_length[middle - (i - middle)]
                else:
                    length = right_max - i
                if i + length < right_max:
                    split_string_palin_length[i] = length
                else:
                    while split_string[i - length] == split_string[i + length]:
                        length += 1
                    split_string_palin_length[i] = length
                    middle = i
                    right_max = i + length - 1
        split_string_palin_length[1] += 1
        split_string_palin_length[-2] += 1
        split_string_palin_length[-1] += 1
        sum = 0
        for i in range(1, len(s) + 1):
            if split_string_palin_length[2 * i - 1] % 2 != 0:
                sum += (split_string_palin_length[2 * i - 1] + 1) / 2
            else:
                sum += split_string_palin_length[2 * i - 1] / 2
            sum += int((split_string_palin_length[2 * i]) / 2)
        return int(sum)


class PalindromicSubstringTest(unittest.TestCase):
    def testCountSubstring(self):
        test = Solution()
        self.assertEqual(test.countSubstrings('aaa'), 6)
        self.assertEqual(test.countSubstrings('bcacb'), 7)
        # self.assertEqual(test.countSubstrings('bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb'),100)


if __name__ == '__main__':
    unittest.main()
