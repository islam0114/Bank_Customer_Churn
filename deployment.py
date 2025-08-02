import numpy as np
import streamlit as st
import pandas as pd
import pickle

Data = pickle.load(open('https://drive.google.com/file/d/1c6gCX7dhERvj0NZWswT4Ks4ZNYjnnamW/view?usp=drive_link', 'rb'))
scaler = pickle.load(open('Deployment/scaler.sav', 'rb'))

st.set_page_config(page_title="Bank Customer Churn", page_icon="🏦", layout="wide")
st.title("Bank Customer Churn App")
st.markdown('Predict whether a customer will churn based on various attributes.')

# Input Form
st.markdown("---")
st.subheader("📝 Enter Customer Data:")

Age = st.number_input("Age (18 ==> 60)", min_value=18, max_value=60,step=1)

No_of_Products = st.number_input("Number of Products (0 ==> 4)", min_value=0, max_value=4,step=1)

Balance = st.number_input("Balance (0 ==> 300k)", min_value=0, max_value=300000,step=1)

mapping_1 = {'No': 0, 'Yes': 1}
Is_Active_Member = st.selectbox('Is Active Member?', list(mapping_1.keys()))
Is_Active_Member = mapping_1[Is_Active_Member]

Estimated_Salary = st.number_input("Estimated Salary (0 ==> 250k)", min_value=0, max_value=250000,step=1)

Credit_Score = st.number_input("Credit Score (400 ==> 900)", min_value=400, max_value=900,step=1)

Tenure = st.number_input("Tenure (0 ==> 10)", min_value=0, max_value=10,step=1)

Geography = st.selectbox("Select Geography", ['France', 'Germany', 'Spain'])
geography_encoded = {'Geography_Germany': 0,'Geography_Spain': 0}
if Geography == 'Germany':
    geography_encoded['Geography_Germany'] = 1
elif Geography == 'Spain':
    geography_encoded['Geography_Spain'] = 1

mapping_2 = {'Male': 0, 'Female': 1}
Gender = st.selectbox('Gender', list(mapping_2.keys()))
Gender = mapping_2[Gender]

mapping_3 = {'No': 0, 'Yes': 1}
Has_Credit_Card = st.selectbox('Has Credit Card?', list(mapping_3.keys()))
Has_Credit_Card = mapping_3[Has_Credit_Card]



df = pd.DataFrame({
    "CreditScore": [Credit_Score],
    "Gender": [Gender],
    "Age": [Age],
    "Tenure": [Tenure],
    "Balance": [Balance],
    "NumOfProducts": [No_of_Products],
    "HasCrCard": [Has_Credit_Card],
    "IsActiveMember": [Is_Active_Member],
    "EstimatedSalary": [Estimated_Salary],
    "Geography_Germany": [geography_encoded['Geography_Germany']],
    "Geography_Spain": [geography_encoded['Geography_Spain']]
}, index=[0])

input_df = df[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]]
input_scaled = scaler.transform(input_df)
input_scaled = pd.DataFrame(input_scaled, columns=input_df.columns)

df = pd.DataFrame({
    "CreditScore": [input_scaled["CreditScore"]],
    "Gender": [Gender],
    "Age": [input_scaled["Age"]],
    "Tenure": [input_scaled["Tenure"]],
    "Balance": [input_scaled["Balance"]],
    "NumOfProducts": [input_scaled["NumOfProducts"]],
    "HasCrCard": [Has_Credit_Card],
    "IsActiveMember": [Is_Active_Member],
    "EstimatedSalary": [input_scaled["EstimatedSalary"]],
    "Geography_Germany": [geography_encoded['Geography_Germany']],
    "Geography_Spain": [geography_encoded['Geography_Spain']]
}, index=[0])

con = st.button("🔍 predict Churn")
if con:
    result = Data.predict(df)
    if result == 1:
        st.write("The customer is likely to churn. ⚠️")
    else:
        st.write("The customer is likely to stay. 😊")
