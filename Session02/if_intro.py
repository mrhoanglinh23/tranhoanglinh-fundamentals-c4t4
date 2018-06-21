yob = int(input("Your year of birth: ")) #input
age = 2018 - yob #process
if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# print("Your age: ", age) #output