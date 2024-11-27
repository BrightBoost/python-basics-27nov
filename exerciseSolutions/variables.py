# Exercises

# 1. Create a variable `patient_name` and assign it the value of a patient's name. Print the variable.
patient_name = "Zia"
print(patient_name)

# 2. Create variables `age` and `temperature` for a patient. Assign them realistic values and print them together in one sentence.
patient_age = 1
patient_temperature = 39

# 3. Calculate the BMI of a patient using variables `weight` (in kg) and `height` (in meters). Print the BMI.
patient_height = 1.75
patient_weight = 700

patient_bmi = patient_weight / patient_height ** 2
print(patient_bmi)

# 4. Assign a Boolean variable `has_fever` based on whether a patient's temperature exceeds 38 degrees. Print the result.
has_fever = patient_temperature > 38
print(has_fever)

# 5. Combine the above into a short script that outputs a summary of the patient’s name, age, BMI, and fever status.
print("*******************")
print("Patient: " + patient_name)
print("Age: " + str(patient_age))
print("Height: " + str(patient_height))
print("Weight: " + str(patient_weight))
print("BMI: " + str(patient_bmi))
print("Fever: " + str(has_fever))
print("*******************")

if has_fever and patient_bmi > 30:
    print("We should def schedule an appointment.")
elif has_fever:
    print("appointment")
elif patient_bmi > 30:
    print("No fever, but let's do a checkup.")
else:
    print("No fever.")


