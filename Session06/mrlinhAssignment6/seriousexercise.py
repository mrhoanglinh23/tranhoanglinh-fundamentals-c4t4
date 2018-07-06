num = int(input("Enter any number: "))
n = 0
for i in range(1, num):
    if(num % i == 0):
        n = n + i
if (n == num):
    print(num, "is a Perfect number!")
else:
    print(num, "is not a Perfect number!")