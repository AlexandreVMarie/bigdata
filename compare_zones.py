import joblib
import pandas as pd
import numpy as np

# Încărcăm modelul antrenat
model = joblib.load('random_forest_model.pkl')

# Exemplu de predicție pentru diferite zone
neighborhoods = ['NridgHt', 'Sawyer', 'CollgCr']

# Definim caracteristicile pentru fiecare zonă
for neighborhood in neighborhoods:
    example_house = pd.DataFrame({
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
        'BsmtFin SF 1': [500],
        'Neighborhood': [neighborhood]  # Adăugăm zona
    })

    # Codificare One-Hot pentru variabilele categorice
    example_house = pd.get_dummies(example_house)

    # Asigură-te că toate coloanele din setul de date de antrenament sunt prezente
    for col in model.feature_names_in_:
        if col not in example_house.columns:
            example_house[col] = 0

    # Rearanjează coloanele în ordinea corectă
    example_house = example_house[model.feature_names_in_]

    # Predicția prețului
    predicted_price = model.predict(example_house)
    print(f"Predicted Price in {neighborhood}: ${predicted_price[0]:,.2f}")
