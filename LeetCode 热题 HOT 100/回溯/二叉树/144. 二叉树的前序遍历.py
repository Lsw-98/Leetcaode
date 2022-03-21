# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]

# 示例 2：
# 输入：root = []
# 输出：[]

# 示例 3：
# 输入：root = [1]
# 输出：[1]

# 示例 4：
# 输入：root = [1,2]
# 输出：[1,2]

# 示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]


def preorderTraversal(root):
  res = list()
  
  def preorder(root):
    if not root:
      return 
    
    res.append(root.val)
    preorder(root.left)
    preorder(root.right)
  
  preorder(root)
  return res


print(preorderTraversal([]))
print(preorderTraversal([]))
print(preorderTraversal([]))
print(preorderTraversal([]))
print(preorderTraversal([]))
