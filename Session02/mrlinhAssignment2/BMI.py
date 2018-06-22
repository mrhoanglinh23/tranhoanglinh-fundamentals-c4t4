height = float(input("Enter height in cm: "))
weight = float(input("Enter weight in kg: "))
BMI = weight/ (height*height)

if BMI < 16:
    print("severely underweight")
elif 16 < BMI < 18.5:
    print("underweight")
elif 18.5 < BMI < 25:
    print("normal")
elif 25 < BMI < 30:
    print("overweight")
elif BMI > 30:
    print("obese")