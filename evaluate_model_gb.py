from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate_model(model, X_test, y_test):
    # Prezice pe setul de testare
    y_pred = model.predict(X_test)

    # Calculează eroarea medie pătratică (MSE) și rădăcina pătrată a acesteia (RMSE)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    return mse, rmse

if __name__ == "__main__":
    from data_loading import load_housing_data
    from data_preprocessing import preprocess_data
    from model_training_forest import tr

    filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
    data = load_housing_data(filepath)
    features, target = preprocess_data(data)
    model, X_test, y_test = train_model(features, target)
    mse, rmse = evaluate_model(model, X_test, y_test)
    print(f"Mean Squared Error: {mse}")
    print(f"Root Mean Squared Error: {rmse}")
