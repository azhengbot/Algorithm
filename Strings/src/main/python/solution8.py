class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1

        is_pre = True

        for num in s:

            if (
                is_pre
                and not num.isnumeric()
                and num != "+"
                and num != "-"
                and num != " "
            ):
                return 0

            if (not is_pre) and (not num.isnumeric()):
                return res * sign

            if is_pre and num == " ":
                continue

            if num == "+" and is_pre:
                sign = 1
                is_pre = False

            if num == "-" and is_pre:
                sign = -1
                is_pre = False

            if num.isnumeric():

                is_pre = False
                res = res * 10 + int(num)

                if res * sign > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif res * sign < -(2 ** 31):
                    return -(2 ** 31)

        return sign * res
