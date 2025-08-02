# Bank Customer Churn Prediction Using Data Science
This project aims to develop a predictive model to identify bank customers who are at risk of churning by analyzing demographic, financial, and behavioral factors. The goal is to provide financial institutions with data-driven insights to enhance customer retention strategies and enable proactive interventions.

----

## 1. Project Overview
Banks face increasing challenges in retaining customers, with churn posing a significant threat to long-term profitability. This project leverages data science techniques to:

- Identify critical risk factors that lead to customer churn

- Build machine learning models to classify customers by churn risk level

- Offer actionable insights to improve customer retention strategies and reduce attrition rates

----

## 2. Dataset Description
Source: Kaggle

The dataset includes a wide variety of features categorized into:

- Personal & Demographic Information:
    `CustomerId`, `Surname`, `Gender`, `Age`, `Geography`

- Financial Factors:
    `CreditScore`, `Balance`, `EstimatedSalary`
  
- Account & Behavioral Attributes:
    `Tenure`, `NumOfProducts`, `HasCrCard`, `IsActiveMember`

- Target Variable:
    `Exited`

----

## 3. Data Preprocessing

- Missing Values: 0
- Categorical Encoding: Applied Label Encoding and one-hot encoding
- Feature Scaling: standardization was applied to continuous variables (`CreditScore`, `Age`, `Balance`, `EstimatedSalary`)
- Train-Test Split: 70% training / 30% testing

----

## 4. Model Development
Multiple machine learning models were tested. Random Forest Model was selected as the final model due to its:

- High accuracy

- Robust performance on imbalanced data

- Capability to capture both linear and non-linear patterns

- Built-in support for feature importance analysis

The final Random Forest model was saved and prepared for deployment.

----

## 5. Model Deployment
Input Features:

- Age (18 ==> 60)

- Number of Products (0 ==> 4)

- Balance (0 ==> 300k)

- Is Active Member?

- Estimated Salary (0 ==> 250k)

- Credit Score (400 ==> 900)

- Tenure (0 ==> 10)

- Select Geography

- Gender

- Has Credit Card?

----

## 6. Challenges Faced
- Imbalanced Target: Required metrics like F1-score and ROC-AUC

- Feature Selection for Plots: Needed to avoid noisy or uninformative visuals

- High Dimensionality: Increased model complexity and training time

- Scaling Issues: Addressed normalization for better visualization and modeling

- Text Data: Required appropriate encoding without losing semantics

- Overfitting Risk: Mitigated with model tuning and feature control

-----

## 7. Key Insights
- Critical Risk Factors Identified: e.g., age, PHQ-9 score, mental health history

- Explainable Models: Feature importance helped interpret predictions

- Proactive Decision Support: Early identification enables better mental health planning

- Deployment-Ready Architecture: Model is scalable and API/web compatible

- Balanced Evaluation Metrics: Focused on precision, recall, F1-score, ROC-AUC

- Insightful Visualizations: Helped uncover patterns and trends in student behavior

----

## 8. Integration Recommendations
- Real-Time Scoring Pipeline: Integrate the model into the bank's CRM or transaction system to score customers in real-time or at regular intervals, identifying high-risk individuals promptly.

- Automated Alerts & Dashboards: Develop dashboards and automated alerts for the customer retention team, enabling proactive outreach when a customer is flagged as high-risk.

- Personalized Retention Strategies: Use model insights (e.g., top churn factors per customer) to tailor offers, discounts, or loyalty programs aimed at reducing churn likelihood.
  
- Model Retraining Schedule: Set up a retraining pipeline to regularly update the model using the latest customer behavior data, ensuring sustained accuracy and relevance.

- Ethical & Regulatory Considerations: Ensure compliance with data privacy regulations (e.g., GDPR) and maintain transparency in automated decision-making processes.

----

## 9. Tools & Technologies

| Category         | Tools                         |
| ---------------- | ----------------------------- |
| Language         | Python                        |
| Data Processing  | pandas, NumPy                 |
| Machine Learning | scikit-learn, XGBoost         |
| Visualization    | Matplotlib, Seaborn, Power BI |

----

## 10. Project Structure
Bank_Customer_Churn/

│

├── CODE/                          # Final scripts and source code

│

├── DATASETS/                      # Processed datasets

│

├── DEPLOYMENT/                    # Deployment logic or configuration

│

├── Dashboard/                     # Power BI dashboards and reports

│

├── deployment.py                  # Bank Customer Churn App

│

├── README.md                      # Project documentation and overview

│

├── requirements.txt               # List of required Python packages

