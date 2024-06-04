import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Încărcăm setul de date
filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
data = pd.read_csv(filepath)

# Generăm box plot pentru Prețurile Locuințelor pe Cartiere
plt.figure(figsize=(14, 8))
sns.boxplot(x='Neighborhood', y='SalePrice', data=data)
plt.title('Distribuția Prețurilor Locuințelor pe Cartiere')
plt.xlabel('Cartier')
plt.ylabel('Prețul Locuinței ($)')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()
