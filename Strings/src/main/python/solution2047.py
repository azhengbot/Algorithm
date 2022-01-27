# https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence
from typing import List


class Solution:
    def countValidWords(self, sentence: str) -> int:

        token_list: List[str] = sentence.split(" ")

        def check_token(token: str) -> bool:
            n = len(token)
            if n == 0:
                return False
            hyphen_count = 0
            for i in range(n):
                if token[i].isdigit():
                    return False
                if token[i].isalpha():
                    continue
                if token[i] == "-":
                    if (
                        hyphen_count == 0
                        and i != 0
                        and i != n - 1
                        and token[i - 1].isalpha()
                        and token[i + 1].isalpha()
                    ):
                        hyphen_count += 1
                        continue
                    else:
                        return False
                if token[i] in ["!", ".", ","]:
                    if i == n - 1:
                        return True
                    else:
                        return False

            return True

        ans = 0

        for token in token_list:
            if check_token(token):
                # print(token)
                ans += 1

        return ans
