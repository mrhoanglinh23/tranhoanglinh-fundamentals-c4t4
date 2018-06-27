number = int(input("Enter a prime number: "))  
  
if number < 2:
    print(number, "Not a prime number")
elif number == 2:
    print( number, "It's a prime number")
else:
    isPrimeNumber = True;
    for i in range(2, number):
        if number % i == 0:
            isPrimeNumber = False;
            break
        
    if isPrimeNumber == True:
        print( number, " Is a prime number")
    else:
        print(number, "Is Not a prime number")
    