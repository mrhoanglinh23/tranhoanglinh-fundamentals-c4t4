x = int(input("x = "))
op = input("Operation (+, -, *, /): ")
y = int(input("y = "))

# calculator
if op == '+':
    res = x + y
elif op == '-':
    res = x - y
elif op == '*':
    res = x * y
elif op == '/':
    res = x / y

print("* " * 10)
print(" {0} {1} {2} = {3}".format(x, op, y, res))
print("* " * 10)


