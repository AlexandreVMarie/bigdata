from sklearn.metrics import mean_squared_error
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Încărcăm setul de date și modelul antrenat
filepath = 'Housing.csv'
data = pd.read_csv(filepath)
model = joblib.load('random_forest_model.pkl')

# Selectăm caracteristicile și variabila țintă
features = data[['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Total Bsmt SF',
                 'Full Bath', 'Year Built', 'Year Remod/Add', '1st Flr SF',
                 '2nd Flr SF', 'Fireplaces', 'Mas Vnr Area', 'BsmtFin SF 1',
                 'Neighborhood']]
target = data['SalePrice']

# Codificare One-Hot pentru variabilele categorice
features = pd.get_dummies(features)

# Completează valorile lipsă cu medianele coloanelor respective
features = features.fillna(features.median())

# Împărțim datele în seturi de antrenament și testare
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Asigură-te că toate coloanele din setul de date de antrenament sunt prezente în setul de testare
for col in X_train.columns:
    if col not in X_test.columns:
        X_test[col] = 0

# Asigură-te că ordinea coloanelor este aceeași
X_test = X_test[X_train.columns]

# Predicția pe setul de testare
y_pred = model.predict(X_test)

# Calcularea MSE și RMSE
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")

# Vizualizarea importanței caracteristicilor
feature_importances = model.feature_importances_
features = X_train.columns
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})

# Sortăm după importanță
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Vizualizare
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.gca().invert_yaxis()
plt.show()
