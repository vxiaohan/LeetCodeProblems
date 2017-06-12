import unittest


class Solution(object):
    def isPalindromic(self, s):
        length = len(s)
        if len(s) == 1:
            return True
        if s[0] != s[-1]:
            return False
        if length >= 4:
            if s[0] != s[-1] or s[1] != s[-2]:
                return False
        if length % 2 == 0:
            set1 = set(s[:int(length / 2)])
            set2 = set(s[int(length / 2):][::-1])
            if set1 == set2:
                list1 = s[:int(length / 2)]
                list2 = s[int(length / 2):][::-1]
                if list1 == list2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            set1 = set(s[:int((length - 1) / 2)])
            set2 = set(s[int((length - 1) / 2) + 1:][::-1])
            if set1 == set2:
                list1 = s[:int((length - 1) / 2)]
                list2 = s[int((length - 1) / 2) + 1:][::-1]
                if list1 == list2:
                    return True
                else:
                    return False
            else:
                return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringList = list(s)
        stringLength = len(stringList)
        if stringLength == 0:
            return ''
        maxLength = 0
        headIndex = 0
        longestString = ''
        while headIndex + maxLength + 1 <= stringLength:
            testLength = maxLength
            while headIndex + testLength + 1 <= stringLength:
                subList = stringList[headIndex:headIndex + testLength + 1]
                if self.isPalindromic(subList):
                    maxLength = testLength
                    longestString = ''.join(subList)
                testLength += 1
            headIndex += 1
        return longestString


class LongestSubstringTestCase(unittest.TestCase):
    def test_isPalindromic(self):
        test = Solution()
        self.assertEqual(test.isPalindromic('bb'), True)
        self.assertEqual(test.isPalindromic('ab'), False)
        self.assertEqual(test.isPalindromic('abba'), True)
        self.assertEqual(test.isPalindromic('hjbjh'), True)
        self.assertEqual(test.isPalindromic('aba'), True)

    def test_longest(self):
        test = Solution()
        self.assertEqual(test.longestPalindrome('bb'), 'bb')
        self.assertEqual(test.longestPalindrome('abba'), 'abba')
        self.assertEqual(test.longestPalindrome('afhjbjh'), 'hjbjh')
        self.assertEqual(test.longestPalindrome(
            "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"),
            "gykrkyg")
        self.assertEqual(test.longestPalindrome(
            "kxuuisplqldxxqanojzyqlaycqwwrpczkymlbpoolybkbluvfkxzzxsoulnfhlhlqzibfhnbryhbkauxsuavnuqlinxrfdwgypsgjmilygtsqptbmfibcfkgdugljwpzjmwnqhtadraplrtlcxeqoniopzbemhkezvadjblpgmyuwlkwilipuccuqfvyzxtoathpnprqphtsiqjlocrmupngjnuskvbzadwxtxchsutumbvidxauotploicaqxegkstdfkyqbmegjhzdrqsuvrspqzbesgzwelrlejlilqvybdjyflbcziqlncddoohurovyuhfhjoyrkxbrvsepxbsivtrahz"),
            "elrle")
        self.assertEqual(test.longestPalindrome(
            "lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"),
            "pnnp")


if __name__ == '__main__':
    unittest.main()
