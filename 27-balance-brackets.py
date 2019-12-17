"""
Given a string of round, curly, square open and closed brackets return if the brackets are balanced are not
"""

def is_balanced(s):
    stack = []

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)

        else:
            if not stack:
                return False

            if (char == ")" and stack[-1] != "(") or (char == "}" and stack[-1] != "{") or (char == "]" and stack[-1] != "["):
                return False
            stack.pop()

    return len(stack) == 0

s = "{}()[{}])"

print(is_balanced(s))
