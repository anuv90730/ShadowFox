height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi >= 30:
    print("Category: Obesity")
elif 25 <= bmi < 30:
    print("Category: Overweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal")
else:
    print("Category: Underweight")