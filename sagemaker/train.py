import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# SageMaker paths
DATA_DIR = "/opt/ml/input/data/train"
MODEL_DIR = "/opt/ml/model"

def main():
    # Load data
    df = pd.read_csv(os.path.join(DATA_DIR, "Teleco-Customer-churn.csv"))

    # Preprocessing
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df.drop('customerID', axis=1, inplace=True)

    # df = pd.get_dummies(df, drop_first=True)
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    categorical_cols = X.select_dtypes(include=['object']).columns
    numericla_cols= X.select_dtypes(exclude=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat',OneHotEncoder(handle_unknown='ignore'),categorical_cols),
            ('num','passthrough',numericla_cols)
        ]
    )

    model = Pipeline(steps=[
        ('preprocessor',preprocessor),
        ('classifier',RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, os.path.join(MODEL_DIR, "model.pkl"))

if __name__ == "__main__":
    main()