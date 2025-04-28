import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
from snowflake_connect import fetch_customer_data

df = fetch_customer_data()

# Prepare features and label
X = df[['Age', 'Income', 'Activityscore']]   # example features
y = df['Churn']   # target variable (1 = churn, 0 = not churn)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'churn_model.pkl')

print("✅ Model trained and saved!")
