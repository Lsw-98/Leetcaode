// 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
// 如果树中有不止一个众数，可以按 任意顺序 返回。
// 假定 BST 满足如下定义：

// 结点左子树中所含节点的值 小于等于 当前节点的值
// 结点右子树中所含节点的值 大于等于 当前节点的值
// 左子树和右子树都是二叉搜索树

// 示例 1：
// 输入：root = [1, null, 2, 2]
// 输出：[2]

// 示例 2：
// 输入：root = [0]
// 输出：[0]


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var findMode = function (root) {
  const obj = {}
  const res = []
  let ans = []
  let num = 0

  function inorder(root) {
    if (root === null) return

    inorder(root.left)
    res.push(root.val)
    inorder(root.right)
  }

  inorder(root)

  for (let index = 0; index < res.length; index++) {
    if (obj[res[index]]) {
      obj[res[index]] += 1
    } else {
      obj[res[index]] = 1
    }
    if (obj[res[index]] > num) {
      ans = []
      num = obj[res[index]]
      ans.push(res[index])
    } else if (obj[res[index]] === num) {
      ans.push(res[index])
    }
  }

  return [ans]
};
