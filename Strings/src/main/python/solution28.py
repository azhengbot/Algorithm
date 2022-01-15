class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        b = 131
        p = 10 ** 9 + 7  # 这两合起来组成一个str转数字的进制

        haystack_pre_hash = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            print(type(haystack_pre_hash[i - 1]))
            haystack_pre_hash[i] = (
                haystack_pre_hash[i - 1] * b % p + ord(haystack[i - 1]) * b % p
            )

        needle_hash = 0
        for ch in needle:
            needle_hash += ord(ch) * b % p

        for left in range(1, n + 1 - m):
            right = left + m - 1

            sub_hay_hash = haystack_pre_hash[right] - haystack_pre_hash[left] * (
                (b % p) ** m
            )
            if sub_hay_hash == needle_hash:
                return left - 1

        return -1


s = Solution()
res = s.strStr("hello", "ll")
print(res)
