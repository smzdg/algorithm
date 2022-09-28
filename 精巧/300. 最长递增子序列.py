# 提交时间：2022/08/09 16:01
# 方法：DP+二分
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [10**4+1 for i in range(len(nums))]
        ans = 0
        for i in nums:
            p = bisect_left(d, i)
            ans = max(ans, p+1)
            d[p] = i
        return ans