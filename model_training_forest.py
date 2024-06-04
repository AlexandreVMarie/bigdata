from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

# Încărcăm și preprocesăm setul de date
filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
data = pd.read_csv(filepath)

# Selectăm un set extins de caracteristici relevante și variabila țintă
features = data[['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Total Bsmt SF',
                 'Full Bath', 'Year Built', 'Year Remod/Add', '1st Flr SF',
                 '2nd Flr SF', 'Fireplaces', 'Mas Vnr Area', 'BsmtFin SF 1',
                 'Neighborhood']]
target = data['SalePrice']

# Codificare One-Hot pentru variabilele categorice
features = pd.get_dummies(features)

# Completează valorile lipsă cu medianele coloanelor respective
features = features.fillna(features.median())

# Împărțirea datelor în seturi de antrenament și testare
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Crearea și antrenarea modelului Random Forest
model = RandomForestRegressor(n_estimators=1000, random_state=42)
model.fit(X_train, y_train)

# Salvăm modelul antrenat pentru evaluare
joblib.dump(model, 'random_forest_model.pkl')
print("Model trained and saved as 'random_forest_model.pkl'")
