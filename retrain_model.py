# retrain_model.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1. Load dataset
df = pd.read_excel("emotion_data.csv.xlsx")  # replace with your CSV filename

# 2. Split features and labels
X = df.drop("emotion", axis=1)  # input features
y = df["emotion"]               # target labels

# 3. Split into train/test (optional but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Save the model
joblib.dump(model, "emotion_model.joblib")

print("✅ Model retrained and saved as emotion_model.joblib.")
