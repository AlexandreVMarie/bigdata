import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_feature_importance(model, features):
    importance = model.feature_importances_
    feature_importance = pd.DataFrame({'Feature': features.columns, 'Importance': importance})
    feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importance)
    plt.title('Feature Importance')
    plt.show()

if __name__ == "__main__":
    from data_loading import load_housing_data
    from data_preprocessing import preprocess_data
    from model_training_forest import train_model

    filepath = 'Housing.csv'  # Actualizează această cale după cum este necesar
    data = load_housing_data(filepath)
    features, target = preprocess_data(data)
    model, X_test, y_test = train_model(features, target)

    plot_feature_importance(model, features)
