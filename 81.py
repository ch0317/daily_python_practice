# 已知存在一个按非降序排列的整数数组
# nums ，数组中的值不必互不相同。
#
# 在传递给函数之前，nums
# 在预先未知的某个下标
# k（0 <= k < nums.length）上进行了
# 旋转 ，使数组变为[nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1], ..., nums[k - 1]]（下标
# 从
# 0
# 开始
# 计数）。例如， [0, 1, 2, 4, 4, 4, 5, 6, 6, 7]
# 在下标
# 5
# 处经旋转后可能变为[4, 5, 6, 6, 7, 0, 1, 2, 4, 4] 。
#
# 给你
# 旋转后
# 的数组
# nums
# 和一个整数
# target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果
# nums
# 中存在这个目标值
# target ，则返回
# true ，否则返回
# false 。
#
# 你必须尽可能减少整个操作步骤。
#
#
#
# 示例
# 1：
#
# 输入：nums = [2, 5, 6, 0, 0, 1, 2], target = 0
# 输出：true
# 示例
# 2：
#
# 输入：nums = [2, 5, 6, 0, 0, 1, 2], target = 3
# 输出：false

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target

        left, right = 0, n - 1
        while left <= right:

            mid = left + (right - left) // 2
            printf(mid)
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    left = mid + 1  # target 在右侧
                else:
                    right = mid - 1  # target 在左侧


        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    print(Solution().search(nums, 3))  # Corrected instantiation