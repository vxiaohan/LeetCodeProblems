import unittest


class Solution:
    def zigzag(self, s_len, numRows):
        index = list(range(numRows))
        reverse = True
        index_order = range(1, numRows)
        reverse_index = range(numRows)[-2::-1]
        while(len(index) < s_len):
            if(reverse):
                index.extend(reverse_index)
                reverse = False
            else:
                index.extend(index_order)
                reverse = True
        return index[:s_len:]


    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        result = ""
        print(s)
        resultTemp = []
        for i in range(numRows):
            resultTemp.append([])
        index = self.zigzag(len(s), numRows)
        for i in range(len(s)):
            resultTemp[index[i]].append(s[i])
        for i in range(numRows):
            result += "".join(resultTemp[i])
        return result


class ZigZagConversionTestCase(unittest.TestCase):
    def testZigZag(self):
        test=Solution()
        self.assertEqual(test.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(test.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")


if __name__ == '__main__':
    unittest.main()

