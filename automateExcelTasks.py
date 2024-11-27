import pandas as pd

# Example data
data = {
    'Patient': ['Zia', 'Lara', 'Lynn'],
    'Dosage (mg)': [150, 200, 180]
}

df = pd.DataFrame(data)

# Write to Excel
df.to_excel("medication_report.xlsx", index=False)
print("Medication report saved to Excel.")
