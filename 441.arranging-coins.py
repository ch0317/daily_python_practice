# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
#
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

# 输入：n = 5
# 输出：2
# 解释：因为第三行不完整，所以返回 2 。
#
#
# 输入：n = 8
# 输出：3
# 解释：因为第四行不完整，所以返回 3 。


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = l + (r - l) // 2
            cost = m*(m + 1) // 2
            if cost == n:
                return m
            elif cost > n:
                r = m - 1
            else:
                l = m + 1
        return r

if __name__ == '__main__':
    s = Solution()

    print(s.arrangeCoins(5))   # 输出 2
    print(s.arrangeCoins(8))   # 输出 3
    print(s.arrangeCoins(1))   # 输出 1
    print(s.arrangeCoins(0))   # 输出 0
    print(s.arrangeCoins(3))   # 输出 2
    print(s.arrangeCoins(1804289383))  # 较大的 n