import pandas as pd


def preprocess_data(data):
    # Selectează un set extins de caracteristici relevante și variabila țintă
    features = data[['Overall Qual', 'Gr Liv Area', 'Garage Cars', 'Total Bsmt SF',
                     'Full Bath', 'Year Built', 'Year Remod/Add', '1st Flr SF',
                     '2nd Flr SF', 'Fireplaces', 'Mas Vnr Area', 'BsmtFin SF 1']]
    target = data['SalePrice']

    # Completează valorile lipsă cu medianele coloanelor respective
    features = features.fillna(features.median())

    return features, target


if __name__ == "__main__":
    from data_loading import load_housing_data

    filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
    data = load_housing_data(filepath)
    features, target = preprocess_data(data)
    print(features.head())
    print(target.head())
