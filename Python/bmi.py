height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kg: "))
bmi=(weight/height**2)
if(bmi<18.5):
    print(f"Your BMI is",bmi, "Unerweight")
elif(bmi>18.5 and bmi<24.9):
    print(f"Your BMI is",bmi, "Healthy")
elif(bmi>25 and bmi<29.9):
    print(f"Your BMI is",bmi,"Overweight")
else:
    print(f"Your BMI is",bmi, "Obese")