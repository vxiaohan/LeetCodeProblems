import unittest


class Solution:
    '''
    # 48ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict = {}
        for letter in J:
            dict[letter] = 0
        for letter in S:
            if letter in dict:
                dict[letter] += 1
        sum = 0
        for k, v in dict.items():
            sum += v
        return sum
    '''

    '''
    48ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict_alpha = {}
        alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
                    "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
                    "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
        for letter in alphabet:
            dict_alpha[letter] = 0
        for letter in S:
            dict_alpha[letter] += 1
        sum = 0
        for letter in set(J):
            sum += dict_alpha[letter]
        return sum
    '''
    '''
    # 44ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict_alpha = {}
        alphabet = set(J + S)
        for letter in alphabet:
            dict_alpha[letter] = 0
        for letter in S:
            dict_alpha[letter] += 1
        sum = 0
        for letter in set(J):
            sum += dict_alpha[letter]
        return sum
    '''
    '''
    # 40ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        for s in S:
            if s in J:
                sum += 1
        return sum
    '''
    # 40ms
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum = 0
        dict_alpha = {}
        for i in J:
            dict_alpha[i] = 0
        for s in S:
            if s in dict_alpha:
                sum = sum + 1
        return sum
class TestJewelsInStons(unittest.TestCase):
    def testNumJewelsInStones(self):
        test = Solution()
        self.assertEqual(test.numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(test.numJewelsInStones("z", "ZZ"), 0)


if __name__ == "__main__":
    unittest.main()
