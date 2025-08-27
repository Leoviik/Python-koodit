Height = float(input("Anna pituutesi"))
Weight = float(input("Anna painosi"))

bmi = Weight / (Height * 100) ** 2
print("Sinun BMI on", bmi)
print(f"Sinun BMI on, {bmi:5.2f}")


