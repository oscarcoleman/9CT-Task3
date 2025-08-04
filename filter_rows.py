import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Global_Education_Cleaned.csv", encoding='ISO-8859-1')

rows = [7, 9, 24, 33, 36, 37, 38, 53, 54, 63, 64, 67, 68, 72, 85, 114, 126, 127, 133, 137, 139, 142, 143, 162, 173, 198]

df = df.iloc[rows, :]

df.to_csv("Global_Ed_Cleaned2.csv", index=False)