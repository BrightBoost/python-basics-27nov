# # Exercises

# 1. Create a list of three patient names and print each name using a loop.
patients = ["patient1", "p2", "p3"]
for patient in patients:
    print(patient)
    
# 2. Create a dictionary for one patient containing their name, age, and medication. Print the dictionary.

patientDict = {
    "name": "Jane",
    "age":27,
    "medication": ["paracetamol"]
}

print(patientDict)

# 3. Extend the dictionary to include a list of vital signs (e.g., temperature readings). Print the updated dictionary.
patientDict = {
    "name": "Jane",
    "age":27,
    "medication": ["paracetamol"],
    "vital_signs": [{"heartbeat": 67}, {"temperature": 37}]
}
print(patientDict)
# 4. Create a list of dictionaries, each representing a patient, and loop through it to print each patient's name and medication.
listPatientDict = [
    {
    "name": "Jane",
    "age":28,
    "medication": ["paracetamol"],
    "vital_signs": [{"heartbeat": 67}, {"temperature": 37}]
    },
    {
    "name": "Johnny",
    "age":27,
    "medication": [],
    "vital_signs": [{"heartbeat": 67}, {"temperature": 37}]
    },
    {
    "name": "Bob",
    "age":25,
    "medication": ["paracetamol", "ibuprofen"],
    "vital_signs": [{"heartbeat": 67}, {"temperature": 37}]
    }
]

for p in listPatientDict:
    print(p["name"], "medications:", p["medication"])
    
# 5. Write a script that calculates the average age of all patients in the list of dictionaries.

sumAges = 0
patientCount = 0

for p in listPatientDict:
    sumAges = sumAges + p["age"]
    patientCount = patientCount + 1
    
print(sumAges / patientCount)

# shorter way

sumAges = 0

for p in listPatientDict:
    sumAges = sumAges + p["age"]

print(sumAges / len(listPatientDict))
