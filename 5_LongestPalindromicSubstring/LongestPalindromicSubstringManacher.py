import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = "#"
        for i in s:
            string += i + "#"
        

class LongestSubstringManacherTestCase(unittest.TestCase):
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
