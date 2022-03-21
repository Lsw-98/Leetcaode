# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。

# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

# 示例 2：
# 输入：nums = [1]
# 输出：1

# 示例 3：
# 输入：nums = [5,4,-1,7,8]
# 输出：23


def maxSubArray(nums):
  dp = [0 for _ in range(len(nums))]
  dp[0] = nums[0]
  maxNum = float("-inf")

  for i in range(1, len(nums)):
    dp[i] = max(nums[i], nums[i] + dp[i - 1])
    if dp[i] > maxNum:
      maxNum = dp[i]
  return maxNum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([5, 4, -1, 7, 8]))
