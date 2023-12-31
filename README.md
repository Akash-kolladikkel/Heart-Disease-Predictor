# Heart Disease Prediction


## Overview
This project aims to predict the presence or absence of heart disease using logistic regression. The model is trained on a dataset obtained from the UCI Machine Learning Repository, and the performance metrics indicate its effectiveness in predicting heart disease.This project provides an interactive and user-friendly interface powered by Streamlit, allowing users to explore the predictions by adjusting the input parameters.

Here is the Screenshots of the webapp:
![ss1](https://github.com/Akash-kolladikkel/Heart-Disease-Predictor/assets/91449571/83b7b6fd-8d1a-4f58-a08c-ee177de32bae)
![ss2](https://github.com/Akash-kolladikkel/Heart-Disease-Predictor/assets/91449571/c6a69e26-96ab-4535-b7ab-6c602486c2cd)


## Dataset
The Heart Disease dataset, available on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease), is a comprehensive collection of health-related attributes with a primary focus on heart disease detection. This dataset originally comprises 76 attributes, but research efforts have commonly utilized a subset of 14 key features. Notably, analyses have predominantly centered around the Cleveland database, which stands as the primary resource in the machine learning community.The "goal" field refers to the presence of heart disease in the patient.  It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0)

## Key Features
- Logistic regression model for heart disease prediction.
- Web app interface for interactive predictions.



## Workflow
- **Data Collection:** The Heart Disease dataset is fetched from the UCI Machine Learning Repository, containing 76 attributes related to heart health.
- **Exploratory Data Analysis (EDA):** Exploring the dataset to understand its structure and visualizing the distribution of the target variable (heart disease presence).
- **Data Preprocessing:** Handling duplicate and null values, imputing missing values, and preparing the data for model training.
- **Model Building:** Utilizing logistic regression to train a model capable of distinguishing between the presence and absence of heart disease.
- **Model Evaluation:** Assessing the model's performance using metrics such as accuracy, precision, recall, and F1 score.
- **Web Application Deployment:** Creating a user-friendly web application using Streamlit for interactive heart disease predictions.

## Performance Metrics
- **Accuracy:** 86.9%
- **Precision:** 90.0%
- **Recall:** 84.4%
- **F1 Score:** 87.1%

