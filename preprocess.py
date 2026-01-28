import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# df = pd.read_csv("/Users/ishika.3.saxena/serverless/churn_prediction/data/Teleco-Customer-churn.csv")
df = pd.read_csv("data/Teleco-Customer-churn.csv")
print("original dataset shape",df.shape)

# handles missing values (TotalCharges sometimes is object due to spaces → convert to numeric)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors='coerce')

# drop rows with missing values
df.dropna(inplace=True)
print("after dropping missing values",df.shape)

duplicates = df.duplicated().sum()
print("number of duplicate rows:",duplicates)
if duplicates > 0:
    df.drop_duplicates()
    print("after removing duplicates",df.shape)

if 'customerID' in df.columns:
    df.drop('customerID',axis=1,inplace=True)

# -------------------------------------------------------------------------
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x='Churn', y=col, data=df)
    plt.title(f'{col} vs Churn')
    plt.show()

df['Churn']=df['Churn'].map({'Yes':1,'No':0})

# encode categorical features
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# split into features and target
X=df.drop('Churn',axis=1)
y=df['Churn']

# train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

X_train.to_csv("data/X_train.csv",index=False)
X_test.to_csv("data/X_test.csv",index=False)
y_train.to_csv("data/y_train.csv",index=False)
y_test.to_csv("data/y_test.csv",index=False)