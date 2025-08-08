# display bar graph for each region, with each country showing their primary and high school scores side-by-side
# display world bar graph that compares the regional averages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Global_Ed_Cleaned2.csv', encoding='ISO-8859-1')

'''

----- TEMPLATE -----

labels = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]
values2 = [12, 18, 22, 28]

x = np.arange(len(labels))  # the label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.legend()
plt.show()

'''

# ----- SCANDANAVIA LITERACY 
'''
rows_scan = [7, 10, 19, 25] 

values1_scan = df.iloc[rows_scan, 1] 
values2_scan = df.iloc[rows_scan, 5]

labels = df.iloc[rows_scan, 0].tolist()

x = np.arange(len(labels))  
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values1_scan, width, label='Mid-Primary School')
ax.bar(x + width/2, values2_scan, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('Scandanavia Student Literary Performance')
ax.legend()
plt.show()

# ----- SCANDANAVIA MATH 

values3_scan = df.iloc[rows_scan, 2] 
values4_scan = df.iloc[rows_scan, 6]

labels = df.iloc[rows_scan, 0].tolist()

x = np.arange(len(labels)) 
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values3_scan, width, label='Mid-Primary School')
ax.bar(x + width/2, values4_scan, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('Scandanavia Student Math Performance')
ax.legend()
plt.show()

# ----- EUROPE LITERACY

rows_eu = [11, 13, 15, 17, 22, 24, 25] 

values1_eu = df.iloc[rows_eu, 1] 
values2_eu = df.iloc[rows_eu, 3]
values3_eu = df.iloc[rows_eu, 5]

labels = df.iloc[rows_eu, 0].tolist()
labels_shifted = labels[:1] + labels[1:]


x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width, values1_eu, width, label='Mid-Primary School')
ax.bar(x, values2_eu, width, label='End-Primary School')
ax.bar(x + width, values3_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score')
ax.set_title('Europe Student Literacy Performance')
ax.legend()
plt.show()

# ----- EUROPE MATH

values1_eu = df.iloc[rows_eu, 2] 
values2_eu = df.iloc[rows_eu, 4]
values3_eu = df.iloc[rows_eu, 6]

labels = df.iloc[rows_eu, 0].tolist()
labels_shifted = labels[:1] + labels[1:]


x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width, values1_eu, width, label='Mid-Primary School')
ax.bar(x, values2_eu, width, label='End-Primary School')
ax.bar(x + width, values3_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score')
ax.set_title('Europe Student Math Performance')
ax.legend()
plt.show()

# ----- CENTRAL AMERICA LITERACY 

rows_ca = [8, 14, 16, 20] 

values1_ca = df.iloc[rows_ca, 1] 
values2_ca = df.iloc[rows_ca, 3]
values3_ca = df.iloc[rows_ca, 5]

labels = df.iloc[rows_ca, 0].tolist()

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values1_ca, width, label='Mid-Primary School')
ax.bar(x, values2_ca, width, label='End-Primary School')
ax.bar(x + width, values3_ca, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('Central America and Carribeans Student Literacy Performance')
ax.legend()
plt.show()

# ----- CENTRAL AMERICA MATH 

values1_ca = df.iloc[rows_ca, 2] 
values2_ca = df.iloc[rows_ca, 4]
values3_ca = df.iloc[rows_ca, 6]

labels = df.iloc[rows_ca, 0].tolist()

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values1_ca, width, label='Mid-Primary School')
ax.bar(x, values2_ca, width, label='End-Primary School')
ax.bar(x + width, values3_ca, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('Central America and Carribeans Student Math Performance')
ax.legend()
plt.show()
'''