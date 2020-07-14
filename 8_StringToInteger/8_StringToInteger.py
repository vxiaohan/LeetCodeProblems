import unittest


class Solution:
    def myAtoi(self, str: str) -> int:
        index = -1
        for i in range(len(str)):
            if str[i] == " ":
                continue
            elif str[i] == "-" or str[i] == "+" or str[i].isdigit():
                index = i
                break
            else:
                return 0
        if index < 0:
            return 0
        end_index = index
        for i in range(index+1,len(str)):
            if str[i].isdigit():
                end_index = i
                continue
            else:
                end_index = i - 1
                break
        negative = False
        if str[index] == "-":
            negative = True
            index += 1
        elif str[index] == "+":
            index += 1
        else:
            pass
        if index > end_index:
            return 0
        elif index == end_index and (str[index] == "-" or str[index] == "+"):
            return 0
        num_str = str[index:end_index+1]
        number = 0
        if negative:
            number = -int(num_str)
            if number < -2147483648:
                return -2147483648
        else:
            number = int(num_str)
            if number > 2147483647:
                return 2147483647
        return number


class StringToIntegerTestCase(unittest.TestCase):
    def testMyAtoi(self):
        test = Solution()
        self.assertEqual(test.myAtoi("42"),42)
        self.assertEqual(test.myAtoi("-42"),-42)
        self.assertEqual(test.myAtoi("4193 with words"), 4193)
        self.assertEqual(test.myAtoi("words and 987"), 0)
        self.assertEqual(test.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(test.myAtoi("3.14159"), 3)

if __name__ == "__main__":
    unittest.main()