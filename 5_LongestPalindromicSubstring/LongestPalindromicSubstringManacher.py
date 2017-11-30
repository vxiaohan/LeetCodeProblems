import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ''
        elif len(s) == 1:
            return s
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
        max_length = max(split_string_palin_length)
        if max_length == 1:
            return split_string[1]
        alpha_max_value = 0
        alpha_max_index = 0
        sharp_max_value = 0
        sharp_max_index = 0
        for i in range(1, len(s)):
            if split_string_palin_length[i * 2 - 1] > alpha_max_value:
                alpha_max_value = split_string_palin_length[i * 2 - 1]
                alpha_max_index = i * 2 - 1
            if split_string_palin_length[i * 2] > sharp_max_value:
                sharp_max_value = split_string_palin_length[i * 2]
                sharp_max_index = i * 2
        sharp_longest = ''.join(split_string[sharp_max_index - sharp_max_value+1: sharp_max_index + sharp_max_value]).replace('-','').replace('#','').replace('+','')
        alpha_longest = ''.join(split_string[alpha_max_index - alpha_max_value+1: alpha_max_index + alpha_max_value]).replace('-','').replace('#','').replace('+','')
        return sharp_longest if len(sharp_longest)>len(alpha_longest) else alpha_longest

class LongestSubstringManacherTestCase(unittest.TestCase):
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
