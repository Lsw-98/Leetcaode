# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

# 示例 1：
# 输入：s = "()"
# 输出：true

# 示例 2：
# 输入：s = "()[]{}"
# 输出：true

# 示例 3：
# 输入：s = "(]"
# 输出：false

# 示例 4：
# 输入：s = "([)]"
# 输出：false

# 示例 5：
# 输入：s = "{[]}"
# 输出：true


def isValid(s):
    stack = []
    lst = list(map(str, s))
    const = ["(", "{", '[']
    for i in lst:
        if i in const:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == "(":
                stack.pop()
            elif i == ']' and stack[-1] == "[":
                stack.pop()
            elif i == '}' and stack[-1] == "{":
                stack.pop()
            else:
                return False
    return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
