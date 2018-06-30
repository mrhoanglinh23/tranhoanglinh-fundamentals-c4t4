print("Hello, my name is Linh and these are my ship sizes")
n = [5, 7, 300, 90, 24, 50, 75]

print(*n, sep=", ")

print("Now my biggest sheep size",max(n),"let's shear it".format(n))

print("After shearing, here is my flock")
n.insert(3, 8)
n.remove(300)
print(n)

for i in range(1):
    print("Month {0}".format(n))
    print("One month has passed , now here is my flock")
    new_sheep = [x+50 for x in n]
    print (new_sheep)

    max_sheep = max(new_sheep)
    print ("Now my biggest sheep has size", max(new_sheep), "let's shear it")

    print ("After shearing, here is my flock: ")
    index = new_sheep.index(max(new_sheep))
    new_sheep[index] = 8
    print (new_sheep)
    

m = max(n)
print("Now my biggest sheep size",m,"let's shear it")

print("My flock has size in total: ", n)
print("I would get", m, "* 2$ = ", m*2, "$")

