# emotion_detector.py

import librosa
import numpy as np
import joblib

model = joblib.load("emotion_model.pkl")

def extract_features(file_path):
    X, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed.reshape(1, -1)

def predict_emotion(file_path):
    features = extract_features(file_path)
    prediction = model.predict(features)[0]
    return prediction
