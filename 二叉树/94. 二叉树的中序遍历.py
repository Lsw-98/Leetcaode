# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]

# 示例 2：
# 输入：root = []
# 输出：[]

# 示例 3：
# 输入：root = [1]
# 输出：[1]

# 示例 4：
# 输入：root = [1,2]
# 输出：[2,1]

# 示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]


def inorderTraversal(self, root):
  res = list()
  def helper(root):
    if not root:
      return 
    helper(root.left)
    res.append(root.val)
    helper(root.right)
  helper(root)
  return res
