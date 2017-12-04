import unittest

'''
# DP solution
# It works with timeout.
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) <= 1:
            return len(pairs)
        list.sort(pairs, key=lambda x: x[1])
        dp = [1] * len(pairs)
        for i in range(1, len(pairs)):
            max_length = 1
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and dp[j] + 1 > max_length:
                    max_length = dp[j] + 1
            dp[i] = max_length
        return max(dp)
'''
#   Greedy
class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) <= 1:
            return len(pairs)
        list.sort(pairs, key=lambda x: x[1])
        count = 0
        end_value = float('-inf')
        for i in range(len(pairs)):
            if pairs[i][0] > end_value:
                count += 1
                end_value = pairs[i][1]
        return count

class MaxLengthChainTest(unittest.TestCase):
    def testFindLongestChain(self):
        test = Solution()
        self.assertEqual(test.findLongestChain([[1, 2], [2, 5], [3, 4]]), 2)
        self.assertEqual(test.findLongestChain(
            [[-65, 387], [668, 840], [856, 980], [-102, 749], [56, 900], [173, 497], [-864, -836], [-978, -954],
             [642, 979], [-339, 207], [457, 699], [453, 830], [93, 444], [221, 317], [-888, 754], [-583, -577],
             [-469, 731], [-181, 859], [833, 921], [-477, 666], [98, 980], [978, 998], [710, 829], [562, 795],
             [-401, 792], [686, 769], [-890, -776], [-249, 512], [-474, 908], [-99, 13], [969, 988], [-636, -499],
             [678, 727], [-253, 589], [716, 891], [-159, 670], [897, 975], [312, 799], [-213, 686], [-538, -297],
             [409, 558], [716, 977], [-879, 687], [21, 460], [-380, 95], [-407, 454], [307, 444], [454, 895],
             [-137, 705], [-833, 231], [411, 523], [-269, -114], [-824, 21], [-459, 394], [-86, 965], [-797, 988],
             [589, 958], [632, 938], [450, 929], [-211, 797], [-859, -846], [-462, -361], [820, 975], [-939, 914],
             [496, 859], [778, 977], [-770, -70], [-722, 58], [436, 765], [-420, -194], [-282, 357], [939, 970],
             [-352, 14], [630, 697], [33, 486], [569, 584], [500, 970], [317, 496], [380, 854], [137, 852], [-123, 725],
             [645, 987], [500, 600], [134, 581], [-554, 611], [-677, 10], [-742, 771], [583, 926], [828, 880],
             [61, 336], [-78, 244], [-889, 128], [-214, 79], [830, 944], [927, 932], [163, 375], [591, 625],
             [-110, 522], [841, 932], [746, 958], [-966, -106], [-319, -310], [913, 954], [794, 868], [-54, 847],
             [-728, -458], [480, 649], [183, 273], [729, 860], [271, 432], [-238, 41], [608, 635], [-110, 316],
             [223, 479], [347, 616], [-65, 480], [413, 925], [111, 922], [-419, 148], [59, 274], [203, 901], [422, 679],
             [850, 898], [391, 743], [-987, 394], [-956, -236], [308, 590], [456, 903], [-820, -779], [446, 732],
             [312, 623], [-349, 393], [541, 819], [-847, -699], [-947, 732], [58, 788], [-3, 313], [250, 443],
             [342, 930], [-47, 492], [347, 381], [-946, -254], [248, 682], [-522, 581], [-632, 656], [481, 953],
             [735, 976], [525, 966], [-264, 401], [-619, 804], [-599, -28], [-78, 638], [-89, 601], [-869, -457],
             [-702, -469], [-430, 127], [-29, 878], [-13, 801], [-263, -215], [191, 742], [-239, -70], [951, 960],
             [-650, 418], [517, 647], [233, 253], [-425, -232], [885, 914], [301, 802], [576, 880], [341, 840],
             [641, 937], [537, 630], [816, 956], [141, 158], [464, 949], [-153, 65], [829, 833], [-210, 297],
             [-679, -519], [-15, 816], [-354, -123], [-241, 467], [571, 923], [-71, 946], [968, 995], [0, 716],
             [-394, 410], [410, 674], [134, 414], [-57, 619], [745, 830], [749, 755], [455, 835], [-433, -103],
             [-415, 570], [-110, 701], [-983, -443], [726, 961], [321, 438], [-974, -178], [362, 408], [542, 630],
             [876, 882], [744, 958], [-220, 589], [940, 945], [893, 982], [823, 871], [-920, 512], [-743, -30],
             [-454, 978], [56, 607], [-11, 933], [423, 485], [712, 901], [952, 961], [-621, -397], [825, 973],
             [-269, 351], [-356, 848], [781, 908], [621, 944], [869, 922], [75, 332], [-470, -42], [414, 872],
             [-308, 124], [-566, -215], [131, 153], [681, 942], [-394, 569], [-469, 971], [-654, -398], [706, 766],
             [759, 938], [-409, 22], [329, 505], [318, 716], [-611, -3], [-814, 493], [711, 908], [473, 929],
             [652, 943], [-652, -515], [-771, -400], [259, 668], [773, 939], [586, 989], [-710, 600], [467, 572],
             [-134, 517], [-871, -629], [400, 563], [-521, 384], [-415, -109], [-482, 599], [611, 703], [-364, -235],
             [-788, -281], [-421, 445], [-865, 347], [-540, 525], [263, 766], [-234, 971], [91, 462], [-420, 425],
             [-871, 503], [439, 871], [767, 900], [155, 633], [-522, -343], [134, 912], [-974, 164], [-843, 343],
             [-570, 426], [-427, 498], [-673, 294], [958, 975], [661, 818], [879, 983], [-280, 184], [372, 525],
             [-209, 896], [758, 828], [-398, 745], [-24, 185], [-139, 845], [608, 747], [-570, 524], [272, 439],
             [-775, 183], [84, 247], [503, 607], [-697, -63], [283, 477], [-17, 676], [-707, -404], [-853, -468],
             [-296, 856], [-263, 67], [504, 703], [-551, 867], [829, 978], [232, 829], [-914, -154], [-62, -33],
             [723, 841], [-994, -112], [486, 708], [-554, 459], [979, 985], [-918, 146], [-395, 843], [-745, 999],
             [-266, -32], [274, 966], [20, 830], [-306, 820], [-204, 308], [-425, -351], [836, 981], [917, 976],
             [-444, 692], [-953, -42], [-566, 277], [-688, 410], [399, 650], [-846, -530], [926, 991], [615, 881],
             [-906, 782], [178, 602], [804, 837], [999, 1000], [929, 954], [-558, 326], [911, 987], [210, 385],
             [-344, 681], [366, 993], [-296, 787], [-970, -446], [-164, 214], [797, 814], [-819, -602], [-88, -41],
             [919, 990], [-840, 176], [793, 1000], [871, 898], [713, 856], [434, 731], [571, 876], [-497, 181],
             [-861, 281], [-997, 177], [737, 948], [-305, 704], [-769, -215], [-475, 700], [445, 933], [-572, 270],
             [-346, 467], [750, 939], [-260, 89], [86, 298], [356, 769], [308, 680], [-773, 826], [-880, 171],
             [189, 585], [13, 302], [751, 826], [58, 787], [550, 960], [697, 763], [300, 395], [-808, 790],
             [-714, -470], [-974, -616], [-791, -56], [-178, 191], [964, 988], [841, 961], [-67, 961], [923, 928],
             [-179, 609], [-546, 715], [324, 638], [-304, 432], [-167, 618], [-329, 489], [964, 987], [-871, 18],
             [-84, 806], [-370, 605], [926, 948], [-583, -317], [-635, -510], [458, 902], [-501, 935], [-868, 660],
             [760, 910], [636, 942], [537, 846], [2, 40], [586, 705], [668, 757], [559, 594], [-961, 577], [-96, 332],
             [260, 500], [-862, 958], [456, 504], [-276, 44], [-607, 242], [-508, 615], [690, 778], [-415, 496],
             [429, 730], [490, 978], [-726, -446], [842, 959], [445, 540], [482, 752], [401, 773], [-756, 349],
             [-225, 807], [346, 761], [-510, 328], [43, 852], [-970, 982], [85, 980], [210, 394], [-807, -211],
             [100, 772], [93, 600], [-256, 873], [-800, -406], [-378, 330], [855, 924], [-629, 677], [526, 968],
             [-424, 289], [894, 987], [-72, -57], [-719, -340], [-307, 406], [199, 492], [-382, 408], [-980, 822],
             [718, 887], [-665, 461], [-377, 471], [743, 812], [-56, 132], [707, 837], [-304, 664], [-78, 218],
             [103, 412], [779, 874], [-946, 977], [-607, -239], [-35, 311], [511, 583], [653, 661], [-347, 151],
             [-611, 994], [-29, 803], [49, 519], [983, 985], [479, 965], [-651, 24], [951, 997], [-328, -248],
             [-634, 121], [-781, 83], [32, 470], [570, 941], [12, 421], [-987, 532], [-12, 443], [-761, 601],
             [-638, -29], [-801, -693], [841, 993], [558, 779], [-571, -113], [131, 237], [98, 992], [-533, -201],
             [284, 807], [586, 667], [-179, 928], [537, 637], [185, 225], [-424, 662], [-755, 537], [-202, -139],
             [-461, 19], [450, 650], [357, 940], [426, 921], [-196, 119], [-941, 902], [377, 888], [-617, -603],
             [-449, 234], [402, 848], [185, 997], [198, 466], [562, 934], [812, 827], [-526, 665], [-859, -402],
             [-467, 24], [-43, 349], [-841, 167], [707, 994], [-694, -632], [610, 720], [-29, 639], [-755, -301],
             [616, 758], [802, 827], [-123, 813], [285, 942], [732, 808], [46, 741], [970, 972], [50, 642], [702, 927],
             [948, 995], [505, 918], [892, 926], [-186, 822], [639, 982], [975, 993], [345, 894], [-750, -596],
             [-372, 103], [593, 594], [8, 305], [-259, -231], [176, 903], [829, 919], [-911, 3], [-140, 634],
             [-688, 458], [198, 364], [418, 565], [533, 642], [-57, 137], [-983, 15], [-858, 167], [-329, 499],
             [-823, 319], [372, 568], [319, 790], [-990, 106], [431, 663], [-201, 687], [-10, 691]]), 33)


if __name__ == '__main__':
    unittest.main()
