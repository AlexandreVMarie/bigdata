import pandas as pd
import matplotlib.pyplot as plt

# Încărcăm setul de date
filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
data = pd.read_csv(filepath)

# Generăm histograma pentru Suprafața Utilă
plt.figure(figsize=(10, 6))
data['Gr Liv Area'].hist(bins=50, edgecolor='black')
plt.title('Distribuția Suprafaței Utile')
plt.xlabel('Suprafața Utilă (mp)')
plt.ylabel('Frecvența')
plt.grid(False)  # Eliminăm grila pentru claritate
plt.show()

