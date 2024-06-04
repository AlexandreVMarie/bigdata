import pandas as pd

# Încărcăm setul de date
filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
data = pd.read_csv(filepath)

# Explorarea statisticilor descriptive
print("Statistici descriptive pentru setul de date:")
print(data.describe())

# Verificarea distribuției valorilor pentru caracteristicile specifice
print("\nDistribuția valorilor pentru 'Overall Qual':")
print(data['Overall Qual'].value_counts())

print("\nStatistici descriptive pentru 'Gr Liv Area':")
print(data['Gr Liv Area'].describe())

print("\nDistribuția valorilor pentru 'Garage Cars':")
print(data['Garage Cars'].value_counts())

print("\nStatistici descriptive pentru 'Total Bsmt SF':")
print(data['Total Bsmt SF'].describe())

print("\nDistribuția valorilor pentru 'Full Bath':")
print(data['Full Bath'].value_counts())

print("\nStatistici descriptive pentru 'Year Built':")
print(data['Year Built'].describe())

print("\nStatistici descriptive pentru 'Year Remod/Add':")
print(data['Year Remod/Add'].describe())

print("\nStatistici descriptive pentru '1st Flr SF':")
print(data['1st Flr SF'].describe())

print("\nStatistici descriptive pentru '2nd Flr SF':")
print(data['2nd Flr SF'].describe())

print("\nDistribuția valorilor pentru 'Fireplaces':")
print(data['Fireplaces'].value_counts())

print("\nStatistici descriptive pentru 'Mas Vnr Area':")
print(data['Mas Vnr Area'].describe())

print("\nStatistici descriptive pentru 'BsmtFin SF 1':")
print(data['BsmtFin SF 1'].describe())
