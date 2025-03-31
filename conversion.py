# Infix to Postfix Conversion
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    result = ''

    for char in expression:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


# Postfix to Infix Conversion
def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op2}{char}{op1})")
    return stack[0]


# Prefix to Postfix Conversion
def prefix_to_postfix(expression):
    stack = []
    expression = expression[::-1]
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + char)
    return ''.join(stack)


# Prefix to Infix Conversion
def prefix_to_infix(expression):
    stack = []
    expression = expression[::-1]
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{char}{op2})")
    return stack[0]


# Postfix to Prefix Conversion
def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(char + op2 + op1)
    return ''.join(stack)


# Infix to Prefix Conversion
def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = ''.join(['(' if char == ')' else ')' if char == '(' else char for char in expression])
    postfix = infix_to_postfix(expression)
    return postfix[::-1]
