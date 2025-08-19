import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Global_Education_Cleaned.csv", encoding='ISO-8859-1') # dataset to be used

rows = [7, 9, 24, 33, 36, 38, 50, 53, 54, 63, 64, 67, 68, 72, 85, 114, 126, 127, 133, 137, 139, 140, 142, 143, 144, 156, 162, 173, 190] # index values for rows in first column, aka desired countries

df = df.iloc[rows, :] # selected information is all columns for rows in rows list

df.to_csv("Global_Ed_Cleaned2.csv", index=False) # moves cleaned data to new file for final analysis