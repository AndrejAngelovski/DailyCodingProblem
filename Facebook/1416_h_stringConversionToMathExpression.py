# Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

# Don't use eval or a similar built-in parser.

# For example, given '-1 + (2 + 3)', you should return 4.

def evaluate_expression(s):
    stack = []
    operand = 0
    result = 0 # For the on-going result
    sign = 1 # 1 means positive, -1 means negative

    for ch in s:
        if ch.isdigit():
            operand = (operand * 10) + int(ch)
        
        elif ch == '+':
            result += sign * operand
            sign = 1
            operand = 0

        elif ch == '-':
            result += sign * operand
            sign = -1
            operand = 0
        
        elif ch == '(':
            # Push the result and sign on to the stack, for later
            stack.append(result)
            stack.append(sign)

            # Reset operand and result, as if new evaluation begins for the new sub-expression
            sign = 1
            result = 0

        elif ch == ')':
            # Evaluate the expression to the left
            # with result and operand
            result += sign * operand

            # ')' marks end of expression within a set of paranthesis
            # Its result is multiplied with sign on top of stack
            # as stack.pop() is the sign before the paranthesis

            result *= stack.pop() # stack pop 1, the sign before the parantheses

            # Then add to the next operand on the top.
            # as stack.pop() is the result calculated before this paranthises - (...)
            result += stack.pop() # stack pop 2, the result calculated before this paranthesis - (...)

            # Reset the operand
            operand = 0

    return result + sign * operand

expression = input("Enter a mathematical expression: ")

print(evaluate_expression(expression))