# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]

# 示例 2：
# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]


def twoSum(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    if nums[right] >= target:
      right -= 1
    else:
      if nums[left] + nums[right] == target:
        return [nums[left], nums[right]]
      elif nums[left] + nums[right] > target:
        right -= 1
      else:
        left += 1


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([10, 26, 30, 31, 47, 60], 40))
