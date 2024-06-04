import pandas as pd
import matplotlib.pyplot as plt

# Încărcăm setul de date
filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
data = pd.read_csv(filepath)

# Generăm diagrama de dispersie pentru Suprafața Utilă și Prețul Locuințelor
plt.figure(figsize=(10, 6))
plt.scatter(data['Gr Liv Area'], data['SalePrice'], alpha=0.5)
plt.title('Relația dintre Suprafața Utilă și Prețul Locuinței')
plt.xlabel('Suprafața Utilă (mp)')
plt.ylabel('Prețul Locuinței ($)')
plt.grid(True)
plt.show()
