# # Exercises

# 1. Write an `if` statement to check if a patient's temperature exceeds 38. Print 'Fever detected!' if true.
# 2. Add an `else` clause to print 'Normal temperature' if the temperature is 38 or below.
# 3. Add an `elif` clause to handle 'Slight fever' for temperatures between 37 and 38.

temperature = 38.5
if temperature > 38:
    print("Fever detected!")
elif temperature > 37 and temperature < 38:
    print("Slight fever.")
else:
    print("Normal temperature.")

# 4. Write a nested `if` statement to check both temperature and age. Print a warning for high-risk patients (e.g., age > 60 and high fever).
age = 65

# demonstrating nested structures, try to avoid where possible (see below)
if temperature > 38:
    print("Fever detected!")
    if age > 60:
        print("High risk patient.")
elif temperature > 37 and temperature < 38:
    print("Slight fever.")
else:
    print("Normal temperature.")

# Without nested if
if temperature > 38 and age > 60:
    print("Fever detected - high risk patient")
elif temperature > 38:
    print("Fever detected")
elif temperature > 37 and temperature < 38:
    print("Slight fever.")
else:
    print("Normal temperature.")

# 5. Create a script that checks multiple conditions (such as fever and BMI, but do freestyle!) and outputs a detailed risk assessment.
