# Patient data
patients = [
    {"name": "Alice", "age": 30, "medication": "DrugA"},
    {"name": "Bob", "age": 45, "medication": "DrugB"}
]

# Access data
for patient in patients:
    print(f"Patient {patient['name']} is taking {patient['medication']}.")
