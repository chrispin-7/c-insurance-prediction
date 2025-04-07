import streamlit as st
from prediction_helper import predict
from PIL import Image
import random

# Set page configuration
st.set_page_config(page_title="Insurance Predictor", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "Prediction"])

# Home Page
if page == "Home":
    st.title("Welcome to the Health Insurance Cost Predictor App")
    st.markdown("This tool predicts insurance premium costs based on personal and medical details.")
    
    # Display resized image
    image = Image.open("homeimage.jpg")  # Updated path
    resized_image = image.resize((650, 400))  # Resize to 650x400 pixels
    st.image(resized_image, caption="Health Insurance - Secure Your Future", use_container_width=False)

# Prediction Page
elif page == "Prediction":
    # Show image only in Prediction panel
    sidebar_image = Image.open("OIP.jpg")  # Updated path
    st.sidebar.image(sidebar_image, use_container_width=True)

    st.title('Health Insurance Cost Predictor')

    categorical_options = {
        'Gender': ['Male', 'Female'],
        'Marital Status': ['Unmarried', 'Married'],
        'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
        'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
        'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
        'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
        'Medical History': [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ],
        'Insurance Plan': ['Bronze', 'Silver', 'Gold']
    }

    # Layout input
    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    with row3[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row3[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row3[2]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    with row4[0]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row4[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    # Input dictionary
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    # Quotes list
    quotes = [
        "“The best time to buy life insurance is always five years ago.”",
        "“You don’t buy life insurance because you are going to die, but because those you love are going to live.”",
        "“Life insurance is not for the people who die, it’s for the people who live.”",
        "“A small investment today can protect your family’s future tomorrow.”",
        "“Life insurance is a love letter to your family.”"
    ]

    # Prediction button
    if st.button('Predict'):
        prediction = predict(input_dict)
        st.success(f'Predicted Health Insurance Cost: ₹{prediction}')
        
        # Show quote only after prediction
        st.info(random.choice(quotes), icon="💡")

