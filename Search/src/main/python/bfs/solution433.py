from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        genes = ["A", "C", "G", "T"]
        depth = {start: 0}

        if end not in bank:
            return -1

        queue = []

        queue.append(start)

        while len(queue) != 0:
            s = queue[0]
            queue.pop(0)  # pop 0 是从前面去除

            for i in range(8):
                for gene in genes:
                    if s[i] == gene:
                        continue
                    ns = s[:i] + gene + s[i + 1 :]
                    if ns not in bank:
                        continue
                    # if depth.get(ns):  # 不能用这个来判断是否有这个key， 因为有0
                    if ns in depth:
                        continue

                    depth[ns] = depth[s] + 1
                    queue.append(ns)

                    if ns == end:
                        return depth[ns]

        return -1


# start = "AACCGGTT"
# end = "AAACGGTA"
# bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

# start = "AAAAAAAA"
# end = "CCCCCCCC"
# bank = [
#     "AAAAAAAA",
#     "AAAAAAAC",
#     "AAAAAACC",
#     "AAAAACCC",
#     "AAAACCCC",
#     "AACACCCC",
#     "ACCACCCC",
#     "ACCCCCCC",
#     "CCCCCCCA",
#     "CCCCCCCC",
# ]
start = "AAAACCCC"
end = "CCCCCCCC"
bank = [
    "AAAACCCA",
    "AAACCCCA",
    "AACCCCCA",
    "AACCCCCC",
    "ACCCCCCC",
    "CCCCCCCC",
    "AAACCCCC",
    "AACCCCCC",
]

s = Solution()
res = s.minMutation(start, end, bank)

print(res)