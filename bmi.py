print("Welcome to the BMI calculator! ")
height = float(input("What is your height in m: "))
weight = float(input("What is your weight in kg: "))
bmi_decimal = height / (weight * weight)
bmi = round(bmi_decimal, 1)

if bmi < 18.5:
    print(f"Your bmi is {bmi},you are underweight. ")
elif bmi < 25:
    print(f"Your bmi is {bmi},you have a normal weight." )
elif bmi < 30:
    print(f"Your bmi is {bmi},you are overweight. ")
elif bmi < 35:
    print(f"Your bmi is {bmi},you are obese.")
else:
    print(f"Your bmi is {bmi},you are clinically obese. ")


