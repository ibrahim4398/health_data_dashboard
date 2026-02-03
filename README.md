# 🩺 Health Monitoring Dashboard

## 📖 Introduction

The **Health Monitoring Dashboard** is a complete data analysis and visualization project developed as part of a technical interview task.  
The goal of this project is to demonstrate the ability to **retrieve, process, analyze, classify, and visualize health-related data** using Python and modern data science tools.

The project follows a **full data pipeline**, starting from raw data retrieval and ending with an interactive dashboard that allows users to explore health insights in a clear and meaningful way.

---

## 🎯 Project Objectives

- Retrieve raw health data from a remote source
- Clean and preprocess unstructured data
- Apply rule-based health labeling
- Train a machine learning model to classify health conditions
- Store processed and classified data
- Build an interactive dashboard for data exploration
- Present results in a clear and user-friendly format

---

## 🗂️ Project Structure

```text
├── fetching_data.py
│   └── Retrieves original health data and saves it locally
│
├── patient_data_raw.json
│   └── Raw health data including sleep, steps, heart rate, calories, and activity
│
├── main.py
│   └── Data preprocessing, labeling, and machine learning classification
│
├── classified_patient_data.csv
│   └── Final dataset containing predicted health categories
│
├── dashboard.py
│   └── Interactive data visualization dashboard
│
├── requirements.txt
│   └── List of required Python dependencies
│
└── README.md
