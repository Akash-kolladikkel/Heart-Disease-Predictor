import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the saved model
model =  pickle.load(open('C:/Users/kolla/Desktop/Folders/SELF PROJECTS/Heart Disease Prediction (LR)/heart_disease_model.sav', 'rb'))

# Define the prediction function
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Convert categorical features to numerical values
    sex = 1 if sex == 'male' else 0
    cp = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}[cp]
    restecg = {0: 0, 1: 1, 2: 2}[restecg]
    exang = 1 if exang == 'yes' else 0
    slope = {0: 0, 1: 1, 2: 2}[slope]
    thal = {0: 1, 1: 2, 2: 3, 3: 3}[thal]

    # Create a DataFrame with the input features
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    # Make predictions using the saved model
    prediction = model.predict(data)

    return prediction

# Define a main function to run the Streamlit web app
def main():
    # Create the Streamlit app
    st.title('Heart Disease Prediction Web App')

    # Create input fields for user input
    age = st.slider('Age', min_value=1, max_value=100, value=50)
    sex = st.selectbox('Sex', ['male', 'female'])
    cp = st.selectbox('Chest pain type', [0, 1, 2, 3, 4])
    trestbps = st.slider('Resting blood pressure', min_value=80, max_value=200, value=120)
    chol = st.slider('Serum cholesterol', min_value=100, max_value=600, value=200)
    fbs = st.selectbox('Fasting blood sugar', [0, 1])
    restecg = st.selectbox('Rest ECG results', [0, 1, 2])
    thalach = st.slider('Maximum heart rate', min_value=60, max_value=220, value=120)
    exang = st.selectbox('Exercise-induced angina', ['yes', 'no'])
    oldpeak = st.slider('ST depression induced by exercise', min_value=0.0, max_value=6.0, value=2.0, step=0.1)
    slope = st.selectbox('ST segment slope', [0, 1, 2])
    ca = st.slider('Number of major vessels colored by fluoroscopy', min_value=0, max_value=4, value=1)
    thal = st.selectbox('Thallium stress test result', [0, 1, 2, 3])

    # Create a button to trigger the prediction
    if st.button('Predict Heart Disease'):
        # Make the prediction
        prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

        # Display the prediction result
        if prediction == 0:
            st.success('Absence of heart disease')
        else:
            st.error('Presence of heart disease')

# Run the Streamlit web app only when the script is run directly
if __name__ == '__main__':
    main()
