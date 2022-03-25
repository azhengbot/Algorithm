from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res_map = {}
        for one in cpdomains:
            one_l = one.split(" ")
            count = int(one_l[0])
            one_domain = one_l[1]

            all_domains = one_domain.split(".")

            if len(all_domains) == 2:
                all_domains = [one_domain, all_domains[-1]]
            if len(all_domains) == 3:
                all_domains = [one_domain, all_domains[-1], ".".join(all_domains[1:3])]

            for domain in all_domains:
                if res_map.get(domain):
                    res_map[domain] += count
                else:
                    res_map[domain] = count

        res_lst = []
        for k, v in res_map.items():
            res = " ".join([str(v), k])
            res_lst.append(res)

        return res_lst


s = Solution()
# cpdomains = ["9001 discuss.leetcode.com"]
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
res = s.subdomainVisits(cpdomains)
print(res)
