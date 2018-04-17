import unittest


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        sub_domain_dict = {}
        for domain_info in cpdomains:
            domain_info_list = domain_info.split(" ")
            number = int(domain_info_list[0])
            domain = domain_info_list[1]
            temp_list = domain.split(".")
            sub_domain = temp_list[-1]
            if sub_domain in sub_domain_dict:
                sub_domain_dict[sub_domain] += number
            else:
                sub_domain_dict[sub_domain] = number
            for i in range(len(temp_list) - 2, -1, -1):
                sub_domain = temp_list[i] + "." + sub_domain
                if sub_domain in sub_domain_dict:
                    sub_domain_dict[sub_domain] += number
                else:
                    sub_domain_dict[sub_domain] = number
        result_list = []
        for k, v in sub_domain_dict.items():
            result_list.append(str(v) + " " + k)
        return result_list


class TestsubdomainVisits(unittest.TestCase):
    def testSubdomainVisits(self):
        test = Solution()
        self.assertListEqual(sorted(test.subdomainVisits(["9001 discuss.leetcode.com"])),
                             sorted(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]))
        self.assertListEqual(
            sorted(test.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])),
            sorted(["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com",
                    "951 com"]))


if __name__ == "__main__":
    unittest.main()
