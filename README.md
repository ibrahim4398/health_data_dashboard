
Health Monitoring Dashboard
the file named (fetching data) contained the first original main that retrive the original data and save it to patient_data_raw.json .

This project was developed as part of an interview task. The objective is to analyze and visualize health data using Python. The project covers data retrieval, preprocessing, machine learning classification, and an interactive dashboard for visualization.

The process begins with retrieving raw health data from Firebase, which is provided in a file called patient_data_raw.json. This data includes various metrics such as sleep duration, steps taken, heart rate, calories, and more. The data is then cleaned and transformed into a structured table using pandas.

Once the data is prepared, it is labeled based on simple health classification rules. Each record is categorized as 'Good', 'Moderate', or 'Poor' depending on factors like sleep quality, heart rate, and physical activity. A Random Forest classifier is then trained using scikit-learn to predict these health categories. The classified data is saved in a file called classified_patient_data.csv.

To make the results accessible and interactive, a web dashboard is built using Dash and Plotly. The dashboard displays several charts including the distribution of health categories, steps by category, sleep duration, active minutes, and average heart rate. When the dashboard is run, it automatically opens in the browser at http://127.0.0.1:8050.

To run this project, you need to have Python installed. Required libraries are listed in the requirements.txt file. You can install them by running 'pip install -r requirements.txt' in the terminal. Then run the main.py file to process the data and train the model. Finally, run dashboard.py to launch the web application.

This project was created by Ibrahim Kerouaz .
