# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
#
# MedianFinder() 初始化 MedianFinder 对象。
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
#
# 示例 1：
#
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
#
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 提示:
#
# -105 <= num <= 105
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 104 次调用 addNum 和 findMedian

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return -self.small[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# 测试用例
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # 2.0

    # 额外测试
    mf = MedianFinder()
    nums = [5, 2, 10, 3, 7]
    for n in nums:
        mf.addNum(n)
        print(f"Added {n}, median is now {mf.findMedian()}")