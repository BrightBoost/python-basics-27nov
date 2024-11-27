import csv

with open("patients.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # Skip row with column names
    for row in csv_reader:
        print(f"Patient {row[0]} is {row[1]} years old and is prescribed {row[2]}.")
