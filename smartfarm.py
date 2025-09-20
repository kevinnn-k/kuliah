from google.colab import files
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
from imblearn.over_sampling import SMOTE
uploaded = files.upload()  # pilih file smart_farm_harvest_data.csv
files.download("smartfarm_model.pkl")

data = pd.read_csv('smart_farm_harvest_data.csv')
print(data.head())
print(data.info())

X = data.drop("harvest_ready", axis=1)  # semua kolom kecuali target
y = data["harvest_ready"]               # kolom target



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

with open("smartfarm_model.pkl", "wb") as f:
    pickle.dump(model, f)
# Load model
with open("smartfarm_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)




# Urutannya harus sama dengan kolom fitur X
feature_names = X.columns.tolist()

new_data = pd.DataFrame([[70, 6.5, 3.2, 28, 60, 150]], columns=feature_names)
prediction = loaded_model.predict(new_data)
print("Prediksi:", prediction)

