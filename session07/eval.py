# define
# arguments
def calc(x, y, op):
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y

    return res

# call function
# result = calc(3, 7, "+")
# print(result)