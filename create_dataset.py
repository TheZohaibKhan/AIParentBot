import pandas as pd

data = {
    "pitch": [220, 120, 200, 100, 180, 130, 170, 115],
    "intensity": [0.85, 0.45, 0.80, 0.40, 0.70, 0.50, 0.60, 0.42],
    "zero_crossing_rate": [0.05, 0.03, 0.06, 0.02, 0.04, 0.03, 0.04, 0.02],
    "spectral_centroid": [3200, 1500, 2900, 1200, 2500, 1600, 2400, 1400],
    "emotion": ["happy", "sad", "happy", "sad", "neutral", "angry", "neutral", "angry"]
}

df = pd.DataFrame(data)
df.to_csv("emotion_data.csv", index=False)

print("Dataset saved as emotion_data.csv.xlsx")
