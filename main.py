import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Global_Education.csv')

columns = ['Latitude', 
           'Longitude', 
           'OOSR_Pre0Primary_Age_Male', 
           'OOSR_Pre0Primary_Age_Female', 
           'OOSR_Primary_Age_Male', 
           'OOSR_Primary_Age_Female',
           'OOSR_Lower_Secondary_Age_Male',
           'OOSR_Lower_Secondary_Age_Female',
           'OOSR_Upper_Secondary_Age_Male',
           'OOSR_Upper_Secondary_Age_Female',
           'Completion_Rate_Primary_Male',
           'Completion_Rate_Primary_Female',
           'Completion_Rate_Lower_Secondary_Male',
           'Completion_Rate_Lower_Secondary_Female',
           'Completion_Rate_Upper_Secondary_Male',
           'Completion_Rate_Upper_Secondary_Female',
           'Birth_Rate',
           'Gross_Primary_Education_Enrollment',
           'Gross_Tertiary_Education_Enrollment',
           'Unemployment_Rate'
]

df = df.drop(columns)

df.to_csv('Global_Education_Cleaned.csv', index=False)