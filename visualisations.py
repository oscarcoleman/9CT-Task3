# display bar graph for each region, with each country showing their primary and high school scores side-by-side
# display world bar graph that compares the regional averages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Global_Ed_Cleaned2.csv', encoding='ISO-8859-1')


# ----- SCANDANAVIA LITERACY 

rows_scan = [6, 9, 18, 27] 

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
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Scandanavia Student Literary Performance')
ax.legend()
plt.savefig('scan_literacy.png')

# ----- SCANDANAVIA MATH 

values3_scan = df.iloc[rows_scan, 2] 
values4_scan = df.iloc[rows_scan, 6]

x = np.arange(len(labels)) 
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values3_scan, width, label='Mid-Primary School')
ax.bar(x + width/2, values4_scan, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Scandanavia Student Math Performance')
ax.legend()
plt.savefig('scan_math.png')

# ----- EUROPE LITERACY

rows_eu = [10, 12, 14, 16, 22, 23, 26] 

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
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Europe Student Literacy Performance')
ax.legend()
plt.savefig('eu_literacy.png')

# ----- EUROPE MATH

values4_eu = df.iloc[rows_eu, 2] 
values5_eu = df.iloc[rows_eu, 4]
values6_eu = df.iloc[rows_eu, 6]

x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width, values4_eu, width, label='Mid-Primary School')
ax.bar(x, values5_eu, width, label='End-Primary School')
ax.bar(x + width, values6_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Europe Student Math Performance')
ax.legend()
plt.savefig('eu_math.png')

# ----- CENTRAL AMERICA LITERACY 

rows_ca = [7, 13, 15, 19] 

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
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Central America and Carribeans Student Literacy Performance')
ax.legend()
plt.savefig('ca_literacy.png')

# ----- CENTRAL AMERICA MATH 

values4_ca = df.iloc[rows_ca, 2] 
values5_ca = df.iloc[rows_ca, 4]
values6_ca = df.iloc[rows_ca, 6]

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values4_ca, width, label='Mid-Primary School')
ax.bar(x, values5_ca, width, label='End-Primary School')
ax.bar(x + width, values6_ca, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Central America and Carribeans Student Math Performance')
ax.legend()
plt.savefig('ca_math.png')

# ----- SOUTH AMERICA LITERACY 

rows_sa = [0, 2, 4, 5, 8, 20, 21] 

values1_sa = df.iloc[rows_sa, 1] 
values2_sa = df.iloc[rows_sa, 3]
values3_sa = df.iloc[rows_sa, 5]

labels = df.iloc[rows_sa, 0].tolist()

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values1_sa, width, label='Mid-Primary School')
ax.bar(x, values2_sa, width, label='End-Primary School')
ax.bar(x + width, values3_sa, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('South America Student Literacy Performance')
ax.legend()
plt.savefig('sa_literacy.png')

# ----- SOUTH AMERICA MATH 

values4_sa = df.iloc[rows_sa, 2] 
values5_sa = df.iloc[rows_sa, 4]
values6_sa = df.iloc[rows_sa, 6]

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values4_sa, width, label='Mid-Primary School')
ax.bar(x, values5_sa, width, label='End-Primary School')
ax.bar(x + width, values6_sa, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('South America Student Math Performance')
ax.legend()
plt.savefig('sa_math.png')

# ----- MIDDLE EAST LITERACY 

rows_me = [11, 24, 25, 28] 

values1_me = df.iloc[rows_me, 1] 
values2_me = df.iloc[rows_me, 5]

labels = df.iloc[rows_me, 0].tolist()

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width / 2, values1_me, width, label='Mid-Primary School')
ax.bar(x + width / 2, values2_me, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Middle East Student Literacy Performance')
ax.legend()
plt.savefig('me_literacy.png')

# ----- MIDDLE EAST MATH 

values3_me = df.iloc[rows_me, 2] 
values4_me = df.iloc[rows_me, 6]

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width / 2, values3_me, width, label='Mid-Primary School')
ax.bar(x + width / 2, values4_me, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Middle East Student Math Performance')
ax.legend()
plt.savefig('me_math.png')

# ----- OCEANIA LITERACY 

rows_oc = [1, 17] 

values1_oc = df.iloc[rows_oc, 1] 
values2_oc = df.iloc[rows_oc, 5]

labels = df.iloc[rows_oc, 0].tolist()

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width / 2, values1_oc, width, label='Mid-Primary School')
ax.bar(x + width / 2, values2_oc, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Oceania Student Literacy Performance')
ax.legend()
plt.savefig('oc_literacy.png')

# ----- OCEANIA MATH 

values3_oc = df.iloc[rows_oc, 2] 
values4_oc = df.iloc[rows_oc, 6]

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width / 2, values3_oc, width, label='Mid-Primary School')
ax.bar(x + width / 2, values4_oc, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Oceania Student Math Performance')
ax.legend()
plt.savefig('oc_math.png')

# ----- CANADA LITERACY
rows_can = [3] 

values1_can = df.iloc[rows_can, 1].iloc[0]  # scalar
values2_can = df.iloc[rows_can, 5].iloc[0]  # scalar

# ----- CANADA MATH
values3_can = df.iloc[rows_can, 2].iloc[0]  # scalar
values4_can = df.iloc[rows_can, 6].iloc[0]  # scalar

# ------ AVG REGIONAL SCORES 

# SCANDANAVIA
total_values1_scan = values1_scan.sum()
country_count = len(rows_scan)
avg_total_values1_scan = total_values1_scan / country_count

total_values2_scan = values2_scan.sum()
avg_total_values2_scan = total_values2_scan / country_count

total_values3_scan = values3_scan.sum()
avg_total_values3_scan = total_values3_scan / country_count

total_values4_scan = values4_scan.sum()
avg_total_values4_scan = total_values4_scan / country_count

# EUROPE
total_values1_eu = values1_eu.sum()
country_count = len(rows_eu)
avg_total_values1_eu = total_values1_eu / country_count

total_values2_eu = values2_eu.sum()
avg_total_values2_eu = total_values2_eu / country_count

total_values3_eu = values3_eu.sum()
avg_total_values3_eu = total_values3_eu / country_count

total_values4_eu = values4_eu.sum()
avg_total_values4_eu = total_values4_eu / country_count

total_values5_eu = values5_eu.sum()
avg_total_values5_eu = total_values5_eu / country_count

total_values6_eu = values6_eu.sum()
avg_total_values6_eu = total_values6_eu / country_count

# CENTRAL AMERICA
total_values1_ca = values1_ca.sum()
country_count = len(rows_ca)
avg_total_values1_ca = total_values1_ca / country_count

total_values2_ca = values2_ca.sum()
avg_total_values2_ca = total_values2_ca / country_count

total_values3_ca = values3_ca.sum()
avg_total_values3_ca = total_values3_ca / country_count

total_values4_ca = values4_ca.sum()
avg_total_values4_ca = total_values4_ca / country_count

total_values5_ca = values5_ca.sum()
avg_total_values5_ca = total_values5_ca / country_count

total_values6_ca = values6_ca.sum()
avg_total_values6_ca = total_values6_ca / country_count

# SOUTH AMERICA
total_values1_sa = values1_sa.sum()
country_count = len(rows_sa)
avg_total_values1_sa = total_values1_sa / country_count

total_values2_sa = values2_sa.sum()
avg_total_values2_sa = total_values2_sa / country_count

total_values3_sa = values3_sa.sum()
avg_total_values3_sa = total_values3_sa / country_count

total_values4_sa = values4_sa.sum()
avg_total_values4_sa = total_values4_sa / country_count

total_values5_sa = values5_sa.sum()
avg_total_values5_sa = total_values5_sa / country_count

total_values6_sa = values6_sa.sum()
avg_total_values6_sa = total_values6_sa / country_count

# MIDDLE EAST
total_values1_me = values1_me.sum()
country_count = len(rows_me)
avg_total_values1_me = total_values1_me / country_count

total_values2_me = values2_me.sum()
avg_total_values2_me = total_values2_me / country_count

total_values3_me = values3_me.sum()
avg_total_values3_me = total_values3_me / country_count

total_values4_me = values4_me.sum()
avg_total_values4_me = total_values4_me / country_count

# OCEANIA
total_values1_oc = values1_oc.sum()
country_count = len(rows_oc)
avg_total_values1_oc = total_values1_oc / country_count

total_values2_oc = values2_oc.sum()
avg_total_values2_oc = total_values2_oc / country_count

total_values3_oc = values3_oc.sum()
avg_total_values3_oc = total_values3_oc / country_count

total_values4_oc = values4_oc.sum()
avg_total_values4_oc = total_values4_oc / country_count

# ----- WORLD LITERACY 

values1_w = [
    avg_total_values1_scan,  
    avg_total_values1_eu,    
    avg_total_values1_ca,    
    avg_total_values1_sa,    
    avg_total_values1_me,    
    avg_total_values1_oc,
    values1_can             
] 

values2_w = [
    np.nan,                  
    avg_total_values2_eu,    
    avg_total_values2_ca,    
    avg_total_values2_sa,    
    np.nan,                  
    np.nan,                  
    np.nan                  
] 

values3_w = [
    avg_total_values2_scan,  
    avg_total_values3_eu,    
    avg_total_values3_ca,    
    avg_total_values3_sa,    
    avg_total_values2_me,    
    avg_total_values2_oc,    
    values2_can              
] 

with open("regions.txt", "r") as txt_file:
    lines = txt_file.readlines()

labels = lines[:7]

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values1_w, width, label='Mid-Primary School')
ax.bar(x, values2_w, width, label='End-Primary School')
ax.bar(x + width, values3_w, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('World Student Literacy Performance')
ax.legend()
plt.savefig('world_literacy.png')
plt.show()

# ----- WORLD MATH 

values4_w = [
    avg_total_values3_scan,  
    avg_total_values4_eu,
    avg_total_values4_ca,    
    avg_total_values4_sa,   
    avg_total_values4_me,    
    avg_total_values4_oc,   
    values3_can             
] 

values5_w = [
    np.nan,                 
    avg_total_values5_eu,    
    avg_total_values5_ca,    
    avg_total_values5_sa,   
    np.nan,                 
    np.nan,                  
    np.nan                  
] 

values6_w = [
    avg_total_values4_scan,  
    avg_total_values6_eu,
    avg_total_values6_ca,    
    avg_total_values6_sa,    
    avg_total_values4_me,   
    avg_total_values4_oc,   
    values4_can             
] 

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - width, values4_w, width, label='Mid-Primary School')
ax.bar(x, values5_w, width, label='End-Primary School')
ax.bar(x + width, values6_w, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score')
ax.set_title('World Student Math Performance')
ax.legend()
plt.savefig('world_math.png')
plt.show()
