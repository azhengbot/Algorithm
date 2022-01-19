class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0

        for i in range(n):
            left = i - 1
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            res = right - left - 1

            if res > max_len:
                max_len = res
                start = left + 1

        for i in range(n):
            left = i
            right = i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            res = right - left - 1

            if res > max_len:
                max_len = res
                start = left + 1

        return s[start : start + max_len]
