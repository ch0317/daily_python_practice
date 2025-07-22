# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
# 示例 1：
#
# 输入：x = 4
# 输出：2
# 示例 2：
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
# 提示：
#
# 0 <= x <= 231 - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 0
        r = x // 2 + 1
        while l < r:
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m*m > x:
                r = m
            else:
                l = m + 1

        return l - 1

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(0))  # 0
    print(s.mySqrt(1))  # 1
    print(s.mySqrt(4))  # 2
    print(s.mySqrt(8))  # 2
    print(s.mySqrt(9))  # 3
    print(s.mySqrt(15)) # 3
    print(s.mySqrt(16)) # 4
    print(s.mySqrt(2147395599))  # 46339  （接近 int 最大值）