# train_emotion_model.py

import os
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Set path to your dataset
DATA_PATH = "audio_data/"  # Folder with labeled WAV files

# Labels should match filenames like: happy_1.wav, sad_2.wav, angry_3.wav, etc.
def extract_features(file_path):
    X, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)  # (40,)
    return mfccs_processed

features = []
labels = []

for file_name in os.listdir(DATA_PATH):
    if file_name.endswith(".wav"):
        label = file_name.split("_")[0].lower()
        try:
            feature_vector = extract_features(os.path.join(DATA_PATH, file_name))
            features.append(feature_vector)
            labels.append(label)
        except Exception as e:
            print(f"Failed on {file_name}: {e}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train the classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, "emotion_model.pkl")
print("✅ Model saved as emotion_model.pkl")
