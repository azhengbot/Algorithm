class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)

        def skip_left():
            left = 0
            right = n - 1
            count = True

            while left < right:
                # print(left, right)
                if s[left] != s[right]:
                    if not count:
                        return False
                    left += 1
                    count = False
                    continue

                left += 1
                right -= 1

            return True

        def skip_right():
            left = 0
            right = n - 1
            count = True

            while left < right:
                # print(left, right)
                if s[left] != s[right]:
                    if not count:
                        return False
                    right -= 1
                    count = False
                    continue

                left += 1
                right -= 1

            return True

        print(skip_left(), skip_right())
        return skip_left() or skip_right()


solu = Solution()
s = "ebcbbececabbacecbbcbe"
#   "ebcbbcecabbacecebbcbe'
# s = "atbbga"
res = solu.validPalindrome(s)
print(res)
