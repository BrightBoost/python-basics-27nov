# Writing patient data to a file
patients = ["Zia", "Lynn"]

with open("patients.txt", "a") as file:
    for patient in patients:
        file.write(patient + "\n")

# Reading from the file
with open("patients.txt", "r") as file:
    for line in file:
        print(line.strip())
