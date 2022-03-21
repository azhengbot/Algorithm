class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        n, m = len(haystack), len(needle)
        next_ = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = next_[j - 1]

            if needle[j] == needle[i]:
                j += 1

            next_[i] = j

        j = 0
        for i in range(n):
            while j > 0 and needle[j] != haystack[i]:
                j = next_[j - 1]

            if needle[j] == haystack[i]:
                j += 1

            if j == m:
                return i - m + 1

        return -1


s = Solution()
res = s.strStr("aaabcbcbcaaa", "bcbcbcaaa")
print(res)
