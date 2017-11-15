import unittest


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0, 1]
        if num == 0:
            return [0]
        if num == 1:
            return result
        k = 1
        start = 2 ** k
        pre_list = [1]
        while start <= num:
            pre_list_temp = list(pre_list)
            pre_list.extend(map(lambda x: x + 1, pre_list_temp))
            result.extend(pre_list)
            k += 1
            start = 2 ** k
        return result[0:num + 1]

class CountingBitsTestCase(unittest.TestCase):
    def testCountBits(self):
        test = Solution()
        self.assertEqual(test.countBits(5),[0,1,1,2,1,2])


if __name__ == '__main__':
    unittest.main()
