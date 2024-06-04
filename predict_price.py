# predict_price.py
import joblib
import pandas as pd

# Încărcăm modelul antrenat
model = joblib.load('random_forest_model.pkl')

# Exemplu de caracteristici pentru o locuință specifică
new_house = pd.DataFrame({
    'Overall Qual': [7],
    'Gr Liv Area': [2000],
    'Garage Cars': [2],
    'Total Bsmt SF': [1000],
    'Full Bath': [2],
    'Year Built': [1995],
    'Year Remod/Add': [2005],
    '1st Flr SF': [1200],
    '2nd Flr SF': [800],
    'Fireplaces': [1],
    'Mas Vnr Area': [200],
    'BsmtFin SF 1': [500]
})

# Completează eventualele valori lipsă
new_house = new_house.fillna(new_house.median())

# Predicția prețului
predicted_price = model.predict(new_house)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")

# Completează eventualele valori lipsă
new_house = new_house.fillna(new_house.median())

# Predicția prețului
predicted_price = model.predict(new_house)
print(f"Predicted Price: ${predicted_price[0]:,.2f}")
