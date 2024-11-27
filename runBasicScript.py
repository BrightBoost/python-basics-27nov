# Calculate BMI for a patient
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


weight = 70  
height = 1.75  
print(f"The BMI is: {calculate_bmi(weight, height)}")
