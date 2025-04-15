import requests
import json

# Firebase REST API endpoint
url = "https://firestore.googleapis.com/v1/projects/rn-firebase-ml-test/databases/(default)/documents/patientData"

# Send a GET request to Firebase
response = requests.get(url)

# Check response status
if response.status_code == 200:
    data = response.json()
    # Save the JSON data locally
    with open("patient_data_raw.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Data retrieved and saved to 'patient_data_raw.json'")
else:
    print(f"❌ Failed to retrieve data. Status code: {response.status_code}")
