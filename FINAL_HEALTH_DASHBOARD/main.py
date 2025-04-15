# ===================================
# ✅ Task 1: Retrieve Data from JSON
# ===================================
import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the downloaded Firebase data (simulate retrieval)
with open("patient_data_raw.json") as f:
    raw_data = json.load(f)

# ===================================
# ✅ Task 2: Preprocess & Create Table
# ===================================

# Helper function to extract nested values
def get_nested_value(d, key, subkey=None, is_array=False):
    try:
        if is_array:
            return [float(i.get('doubleValue') or i.get('integerValue')) 
                    for i in d[key]['arrayValue']['values']]
        elif subkey:
            return float(d[key]['mapValue']['fields'][subkey].get('doubleValue') or
                         d[key]['mapValue']['fields'][subkey].get('integerValue'))
        else:
            return float(d[key].get('doubleValue') or d[key].get('integerValue'))
    except:
        return None

# Extract records
records = []
for doc in raw_data['documents']:
    fields = doc['fields']
    date = fields.get('date', {}).get('stringValue', '')

    sleep = fields.get('sleep', {}).get('mapValue', {}).get('fields', {})
    activity = fields.get('activity', {}).get('mapValue', {}).get('fields', {})
    vitals = fields.get('vitals', {}).get('mapValue', {}).get('fields', {})
    nutrition = fields.get('nutrition', {}).get('mapValue', {}).get('fields', {})
    macros = nutrition.get('macros', {}).get('mapValue', {}).get('fields', {}) if nutrition else {}

    heart_rate_list = get_nested_value(vitals, 'heart_rate', is_array=True)
    temp_list = get_nested_value(vitals, 'temperature', is_array=True)

    record = {
        'date': date,
        'sleep_duration': get_nested_value(sleep, 'duration_hours'),
        'sleep_interruptions': get_nested_value(sleep, 'interruptions'),
        'sleep_quality': sleep.get('quality', {}).get('stringValue'),

        'steps': get_nested_value(activity, 'steps'),
        'active_minutes': get_nested_value(activity, 'active_minutes'),
        'sedentary_hours': get_nested_value(activity, 'sedentary_hours'),

        'heart_rate_mean': pd.Series(heart_rate_list).mean() if heart_rate_list else None,
        'temperature_mean': pd.Series(temp_list).mean() if temp_list else None,

        'calories': get_nested_value(nutrition, 'calories'),
        'water_oz': get_nested_value(nutrition, 'water_oz'),

        'fat_g': get_nested_value(macros, 'fat_g'),
        'carbs_g': get_nested_value(macros, 'carbs_g'),
        'protein_g': get_nested_value(macros, 'protein_g'),
    }

    records.append(record)

# Build DataFrame
df = pd.DataFrame(records)
print("\n✅ Task 2 - Preprocessed Table:")
print(df.head())

# ===================================
# ✅ Task 3: Label Data & Train Classifier
# ===================================

# Step 1: Label data
def label_health(row):
    if row['sleep_duration'] >= 7.5 and row['heart_rate_mean'] <= 70 and row['steps'] >= 8000:
        return "Good"
    elif row['sleep_duration'] < 6 or row['heart_rate_mean'] > 75 or row['steps'] < 4000:
        return "Poor"
    else:
        return "Moderate"

df['health_label'] = df.apply(label_health, axis=1)

# Step 2: Clean and encode
df_clean = df.dropna()
df_clean['sleep_quality'] = LabelEncoder().fit_transform(df_clean['sleep_quality'])

X = df_clean.drop(['date', 'health_label'], axis=1)
y = df_clean['health_label']

# Step 3: Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Train classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Step 6: Output results
print("\n✅ Task 3 - Classification Report:")
print(classification_report(y_test, y_pred))

# Optional: Save final DataFrame with predictions
df_clean['prediction'] = clf.predict(X_scaled)
df_clean.to_csv("classified_patient_data.csv", index=False)
print("\n📁 Saved: classified_patient_data.csv")
