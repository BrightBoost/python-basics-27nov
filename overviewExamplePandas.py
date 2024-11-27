import pandas as pd

# Sample data: medication effects
data = {
    'Patient': ['A', 'B', 'C'],
    'Medication': ['DrugX', 'DrugY', 'DrugX'],
    'Efficacy': [90, 75, 85]
}

df = pd.DataFrame(data)

average_efficacy = df.groupby('Medication')['Efficacy'].mean()
print("Average Efficacy by Medication:")
print(average_efficacy)
