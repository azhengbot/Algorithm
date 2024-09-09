#
# @lc app=leetcode.cn id=2024 lang=python3
# @lcpr version=30204
#
# [2024] 考试的最大困扰度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        # cnt = Counter(answerKey)
        ans = 0
        cnt = [0, 0]

        i = 0

        for j in range(n):
            if answerKey[j] == "T":
                cnt[0] += 1
            else:
                cnt[1] += 1

            if cnt[0] > k and cnt[1] > k:
                ans = max(ans, j - i)
                print(cnt, i, j)
                if answerKey[i] == "T":
                    cnt[0] -= 1
                else:
                    cnt[1] -= 1
                i += 1

        return max(ans, n - i)


# @lc code=end


#
# @lcpr case=start
# "TTFF"\n2\n
# @lcpr case=end

# @lcpr case=start
# "TFFT"\n1\n
# @lcpr case=end

# @lcpr case=start
# "TTFTTFTT"\n1\n
# @lcpr case=end

#
