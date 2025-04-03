# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
# 示例 1：
#
# 输入：s = "()"
#
# 输出：true
#
# 示例 2：
#
# 输入：s = "()[]{}"
#
# 输出：true
#
# 示例 3：
#
# 输入：s = "(]"
#
# 输出：false
#
# 示例 4：
#
# 输入：s = "([])"
#
# 输出：true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'[':']','(':')','{':'}'}
        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if stack:
                    top_element = stack.pop()
                    if bracket_map[top_element] != c:
                        return False
                else:
                    return False

        return not stack

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("{[()]}", True),
        ("{[(])}", False),
        ("", True),
        ("[", False),
        ("}", False),
        ("{[]}", True)
    ]

    for s, expected in test_cases:
        result = solution.isValid(s)
        print(f"Input: {s}, Output: {result}, Expected: {expected}, Passed: {result == expected}")
