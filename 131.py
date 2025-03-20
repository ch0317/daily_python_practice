# 给你一个字符串
# s，请你将
# s
# 分割成一些子串，使每个子串都是
# 回文串 。返回
# s
# 所有可能的分割方案。
#
#
#
# 示例
# 1：
#
# 输入：s = "aab"
# 输出：[["a", "a", "b"], ["aa", "b"]]
# 示例
# 2：
#
# 输入：s = "a"
# 输出：[["a"]]
#
# 提示：
#
# 1 <= s.length <= 16
# s
# 仅由小写英文字母组成

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        ans = []
        path = []

        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            print(i, start)
            if i == n:
                print(f'append: {path} ')
                ans.append(path.copy())  # 复制 path
                return

            if i < n - 1:
                dfs(i + 1, start)

            t = s[start: i + 1]
            print(f't:{t}')
            if t == t[::-1]:

                path.append(t)
                print(f'path {path}')
                dfs(i + 1, i + 1)
                path.pop()

        dfs(0, 0)
        return ans


if __name__ == '__main__':
    input = "aab"
    print(Solution().partition(input))  # Corrected instantiation