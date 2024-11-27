# Calculate dosage for a medication based on weight
def calculate_dosage(weight, dosage_per_kg):
    return weight * dosage_per_kg


weight = 70  
dosage = calculate_dosage(weight, 2) 
print(f"Dosage required: {dosage}mg")
