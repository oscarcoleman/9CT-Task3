import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Global_Education.csv", encoding='ISO-8859-1') # dataset to be used 

# array contains all columns to be removed
columns = [ 
           'Latitude ',
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
           'Unemployment_Rate',
           'Youth_15_24_Literacy_Rate_Male',
           'Youth_15_24_Literacy_Rate_Female'
]

df = df.drop(columns=columns) # removes columns, as listed in above array, from dataset

df.to_csv('Global_Education_Cleaned.csv', index=False) # moves cleaned data to new file


