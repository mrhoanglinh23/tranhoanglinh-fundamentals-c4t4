n = int(input("Enter a number: "))
for i in range(1,11):
    for j in range(0,n-1, 2):
        print(i*j,end="    ")
    print()
