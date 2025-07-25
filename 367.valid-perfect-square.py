# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#
# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
#
# 不能使用任何内置的库函数，如  sqrt 。
#
#
#
# 示例 1：
#
# 输入：num = 16
# 输出：true
# 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
# 示例 2：
#
# 输入：num = 14
# 输出：false
# 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num // 2 + 1

        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                l = mid + 1
            else:
                r = mid - 1

        return False

if __name__ == '__main__':
    # 创建 Solution 实例
    s = Solution()

    # 测试用例
    test_cases = [
        (0, True),
        (1, True),
        (4, True),
        (9, True),
        (16, True),
        (14, False),
        (25, True),
        (26, False),
        (100, True),
        (101, False),
        (808201, True),  # 899*899
        (2147395600, True),  # 46340*46340
        (2147483647, False)  # INT_MAX
    ]

    # 跑测试
    for num, expected in test_cases:
        result = s.isPerfectSquare(num)
        print(f"num = {num:10} | isPerfectSquare = {result} | expected = {expected} | {'PASS' if result == expected else 'FAIL'}")