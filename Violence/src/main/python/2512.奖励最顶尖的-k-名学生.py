#
# @lc app=leetcode.cn id=2512 lang=python3
#
# [2512] 奖励最顶尖的 K 名学生
#
# https://leetcode.cn/problems/reward-top-k-students/description/
#
# algorithms
# Medium (46.49%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 16.4K
# Testcase Example:  '["smart","brilliant","studious"]\n["not"]\n["this student is studious","the student is smart"]\n[1,2]\n2'
#
# 给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会
# 有单词同时是正面的和负面的。
#
# 一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减  1 分。
#
# 给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中
# student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。每名学生的 ID 互不相同。
#
# 给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。
#
#
#
# 示例 1：
#
# 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback =
# ["not"], report = ["this student is studious","the student is smart"],
# student_id = [1,2], k = 2
# 输出：[1,2]
# 解释：
# 两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
#
#
# 示例 2：
#
# 输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback =
# ["not"], report = ["this student is not studious","the student is smart"],
# student_id = [1,2], k = 2
# 输出：[2,1]
# 解释：
# - ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。
# - ID 为 2 的学生有 1 个正面词汇，得分为 3 分。
# 学生 2 分数更高，所以返回 [2,1] 。
#
#
#
#
# 提示：
#
#
# 1 <= positive_feedback.length, negative_feedback.length <= 10^4
# 1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
# positive_feedback[i] 和 negative_feedback[j] 都只包含小写英文字母。
# positive_feedback 和 negative_feedback 中不会有相同单词。
# n == report.length == student_id.length
# 1 <= n <= 10^4
# report[i] 只包含小写英文字母和空格 ' ' 。
# report[i] 中连续单词之间有单个空格隔开。
# 1 <= report[i].length <= 100
# 1 <= student_id[i] <= 10^9
# student_id[i] 的值 互不相同 。
# 1 <= k <= n
#
#
#

from collections import Counter

# @lc code=start
from typing import List, Set


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        # 做的不好，题解那种先生成一个全部单词的字典实现更好
        pf: Set = set(positive_feedback)
        nf: Set = set(negative_feedback)

        res = [
            sum(
                [
                    (3 * cnt_mp[k]) if k in pf else (-cnt_mp[k] if k in nf else 0)
                    for k in cnt_mp
                ]
            )
            for cnt_mp in [Counter(rep.split(" ")) for rep in report]
        ]
        print(res)

        sort_lst = sorted(
            zip(student_id, res), key=lambda x: [x[1], -x[0]], reverse=True
        )
        return [x[0] for x in sort_lst[:k]]


# @lc code=end
pf = ["fkeofjpc", "qq", "iio"]
nf = ["jdh", "khj", "eget", "rjstbhe", "yzyoatfyx", "wlinrrgcm"]
resport = [
    "rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio",
    "gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx",
    "tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe",
    "jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh",
    "yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq",
    "fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v",
    "wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq",
    "d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe",
]
student_id = [
    96537918,
    589204657,
    765963609,
    613766496,
    43871615,
    189209587,
    239084671,
    908938263,
]
k = 3


s = Solution()
res = s.topStudents(pf, nf, resport, student_id, k)
print(res)
