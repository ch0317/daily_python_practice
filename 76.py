# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。


from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        print(need)
        window = defaultdict(int)

        left, right = 0, 0
        start = 0
        valid = 0
        min_length = float('inf')

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < min_length:
                    min_length = right - left
                    start = left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_length == float('inf') else s[start:start + min_length]








        # 这个题是经典的滑动窗口问题，核心思想是用两个指针（left 和 right）维护一个窗口，
        # 不断移动 right 扩大窗口，直到窗口满足条件（包含 t 所有字符且数量足够），
        # 然后移动 left 缩小窗口以找到最小解。

        # 初始化：
        # need = {'A':1, 'B':1, 'C':1}
        # window = {}
        # left = 0, right = 0
        # valid = 0
        # min_len = inf
        # start = 0
        #
        # 循环：
        # |A|D|O|B|E|C|O|D|E|B|A|N|C|   <-- s 串
        #  ^right
        # - 加入 'A'，window = {'A':1}，valid += 1 （因为 'A' 满足）
        #
        # 继续右移，直到 window 里 'A', 'B', 'C' 都满足 need：
        #
        # |A|D|O|B|E|C|O|D|E|B|A|N|C|
        #              ^right
        # window = {'A':1, 'B':1, 'C':1}
        # valid = 3 (和 need 长度相同，满足条件)
        #
        # 尝试收缩：
        # - left=0 时，窗口长度 6（"ADOBEC"）
        # - 移除 'A'，valid -= 1，窗口不满足了
        #
        # 继续扩张：
        # - right 继续往后，找到新的满足条件
        # - 每次满足条件时尝试收缩更新 min_len
        #
        # 最终找到最小的 window：
        # "BANC"，起始位置 start=9，长度 4



if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # 输出 "BANC"
    print(sol.minWindow("a", "a"))  # 输出 "a"
    print(sol.minWindow("a", "aa"))  # 输出 ""