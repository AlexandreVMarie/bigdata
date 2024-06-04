# data_loading.py
import pandas as pd
pd.set_option('display.max_columns', None)  # Asigură afișarea tuturor coloanelor


def load_housing_data(filepath):
    data = pd.read_csv(filepath)
    return data


if __name__ == "__main__":
    filepath = 'Housing.csv'  # Update this path as needed
    data = load_housing_data(filepath)
    print(data.head())