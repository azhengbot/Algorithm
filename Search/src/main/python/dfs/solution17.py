from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        new_str = ""

        def search(idx):
            nonlocal new_str
            if idx == len(digits):
                ans.append(new_str)
                return

            for i in map[digits[idx]]:
                new_str += i
                search(idx + 1)
                new_str = new_str[0:-1]

        search(0)

        return ans