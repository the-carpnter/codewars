def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/' and num2 != 0:
        return num1 / num2
