import unittest


class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1_value = [ord(s1[i]) for i in range(len(s1))]
        s2_value = [ord(s2[i]) for i in range(len(s2))]

        row_num = len(s1)
        column_num = len(s2)
        if row_num == 0 and column_num == 0:
            return 0
        elif row_num == 0:
            return sum(s2_value)
        elif column_num == 0:
            return sum(s1_value)
        row_num += 1
        column_num += 1
        distance = [[0 for j in range(column_num)] for i in range(row_num)]
        distance[0][0] = 0
        for i in range(1, row_num):
            distance[i][0] = distance[i - 1][0] + s1_value[i - 1]
        for j in range(1, column_num):
            distance[0][j] = distance[0][j - 1] + s2_value[j - 1]
        for i in range(1, row_num):
            for j in range(1, column_num):
                diff = 0 if s1_value[i - 1] == s2_value[j - 1] else s1_value[i - 1] + s2_value[j - 1]
                distance[i][j] = min([distance[i - 1][j - 1] + diff, distance[i][j - 1] + s2_value[j - 1],
                                      distance[i - 1][j] + s1_value[i - 1]])
        return distance[-1][-1]


class MinimunASCIITest(unittest.TestCase):
    def testMinimunDeleteSum(self):
        test = Solution()
        self.assertEqual(test.minimumDeleteSum('sea', 'eat'), 231)
        self.assertEqual(test.minimumDeleteSum('delete', 'leet'), 403)


if __name__ == '__main__':
    unittest.main()
