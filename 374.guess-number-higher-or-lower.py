# 我们正在玩猜数字游戏。猜数字游戏的规则如下：
#
# 我会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
#
# 如果你猜错了，我会告诉你，我选出的数字比你猜测的数字大了还是小了。
#
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有三种可能的情况：
#
# -1：你猜的数字比我选出的数字大 （即 num > pick）。
# 1：你猜的数字比我选出的数字小 （即 num < pick）。
# 0：你猜的数字与我选出的数字相等。（即 num == pick）。
# 返回我选出的数字。
#
#
#
# 示例 1：
#
# 输入：n = 10, pick = 6
# 输出：6
# 示例 2：
#
# 输入：n = 1, pick = 1
# 输出：1
# 示例 3：
#
# 输入：n = 2, pick = 1
# 输出：1

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

picked = 6  # 你可以随便改这个值来测试

def guess(num: int) -> int:
    if num == picked:
        return 0
    elif num < picked:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m - 1
        return l

# 测试用例
if __name__ == "__main__":
    n = 10  # 1 ~ 10
    solution = Solution()
    result = solution.guessNumber(n)
    print(f"Guessed Number: {result}")  # 应该输出 picked 的值
    assert result == picked