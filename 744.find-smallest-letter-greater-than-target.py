# 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
#
# 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
#
#
#
# 示例 1：
#
# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
# 解释：letters 中字典上比 'a' 大的最小字符是 'c'。
# 示例 2:
#
# 输入: letters = ["c","f","j"], target = "c"
# 输出: "f"
# 解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
# 示例 3:
#
# 输入: letters = ["x","x","y","y"], target = "z"
# 输出: "x"
# 解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
#
#
# 提示：
#
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)

        while l < r:
            m = l + (r - l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1

        if l == len(letters):
            return letters[0]
        else:
            return letters[l]

if __name__ == '__main__':
    s = Solution()

    print(s.nextGreatestLetter(["c", "f", "j"], "a"))  # 输出: c
    print(s.nextGreatestLetter(["c", "f", "j"], "c"))  # 输出: f
    print(s.nextGreatestLetter(["c", "f", "j"], "d"))  # 输出: f
    print(s.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # 输出: x
    print(s.nextGreatestLetter(["a", "b"], "z"))  # 输出: a
    print(s.nextGreatestLetter(["a", "b"], "a"))  # 输出: b
    print(s.nextGreatestLetter(["a", "b"], "b"))  # 输出: a