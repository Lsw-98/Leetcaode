# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。

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


def inorderTraversal(root):
  res = list()

  def inorder(root):
    if not root:
      res.append(root.val)
      return
    
    inorder(root.left)
    res.append(root.val)
    inorder(root.right)
  
  inorder(root)
  return res