print("Hello, my name is Linh and these are my ship sizes")
n = [5, 7, 300, 90, 24, 50, 75]

print(*n, sep=", ")

print("Now my biggest sheep size",max(n),"let's shear it")

print("After shearing, here is my flock")
n.insert(4, 8)
n.remove(300)
print(n)

print("""MONTH 1:
One month has passed, now here is my flock
""")
for i in range(4):
    for j in range(7):
        n +=50
