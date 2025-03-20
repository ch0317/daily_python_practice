# 给定一个整数数组
# nums ，数组中的元素
# 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集
# 不能
# 包含重复的子集。你可以按
# 任意顺序
# 返回解集。

# 示例
# 1：
#
# 输入：nums = [1, 2, 3]
# 输出：[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# 示例
# 2：
#
# 输入：nums = [0]
# 输出：[[], [0]]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        l = len(nums)

        def dfs(sub, index):
            print(f'l:{l}, index:{index}')
            if index == l:
                res.append(sub[:])  # Append a copy of sub
                print(f'append: {sub}')
                return
            sub.append(nums[index])
            dfs(sub, index + 1)
            sub.pop()
            dfs(sub, index + 1)

        dfs([], 0)

        return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))  # Corrected instantiation