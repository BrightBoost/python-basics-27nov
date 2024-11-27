# Writing patient data to a file
patients = ["Zia, 30, DrugA", "Lynn, 45, DrugB"]

with open("patients.txt", "w") as file:
    for patient in patients:
        file.write(patient + "\n")

# Reading from the file
with open("patients.txt", "r") as file:
    for line in file:
        print(line.strip())
