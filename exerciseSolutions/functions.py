# 1. Write a function `greet_patient` that takes a patient's name as an argument and prints a greeting.
def greet_patient(name):
    print("Hello", name)


greet_patient("Zia")

# 2. Write a function `calculate_bmi` that takes weight and height as arguments and returns the BMI.
# 3. Extend `calculate_bmi` to categorize the BMI into 'Underweight', 'Normal', 'Overweight', or 'Obese'.

def calculate_bmi(weight, height):

    bmi = weight / height ** 2
    category = 'normal'
    if bmi > 35:
        category = 'obese'
    elif bmi < 18:
        category = 'underweight'
    elif bmi > 25 and bmi < 35:
        category = 'overweight'
    
    return category, bmi

patient_weight = float(input("Weight please."))
patient_height = float(input("Height please."))

result = calculate_bmi(patient_weight, patient_height)
print(result)

print()
# 4. Write a function `risk_assessment` that takes temperature and BMI and returns a risk level (low, medium, high).
# 5. Combine the above functions into a mini program that greets the patient, calculates their BMI, and provides a risk level.